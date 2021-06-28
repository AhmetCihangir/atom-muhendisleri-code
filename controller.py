from flask import Flask,render_template,redirect,url_for,request,flash,session
import wtforms
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from wtforms import form
import yapay_zeka
import yapay_zeka_test
from random import shuffle


app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = 'cihangir'#loginde ekliyoz flash da var

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'karistiran'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def YapayZeka():
    YapayZeka_def = yapay_zeka.YapayZeka()
    YapayZeka_def
    return [YapayZeka_def.txt,YapayZeka_def.cevap]

def YapayZekaTest():
    YapayZekaTest_def = yapay_zeka_test.YapayZekaTest()
    return YapayZekaTest_def

class SignupForm(wtforms.Form):
    karistiran_name = wtforms.StringField('Name',validators=[wtforms.validators.DataRequired()])
    karistiran_username = wtforms.StringField('Username',validators=[wtforms.validators.DataRequired(),wtforms.validators.Length(min=6,max=25)])
    karistiran_email = wtforms.StringField('Email',validators=[wtforms.validators.DataRequired(),wtforms.validators.Email()])
    karistiran_password = wtforms.PasswordField('Password',validators=[wtforms.validators.DataRequired(),wtforms.validators.Length(min=4,max=12)])
    karistiran_language = wtforms.RadioField('Dil',validators=[wtforms.validators.DataRequired()],choices=[('TR','TR'),('EN','EN')])

class LoginForm(wtforms.Form):
    giris_username = wtforms.StringField('Username',validators=[wtforms.validators.DataRequired(),wtforms.validators.Length(min=6,max=25)])
    giris_password = wtforms.PasswordField('Password',validators=[wtforms.validators.DataRequired(),wtforms.validators.Length(min=4,max=12)])

class AnswerFrom(wtforms.Form):
    answer_question = wtforms.StringField('Answer')
    timer = wtforms.IntegerField("Timer")



@app.route("/")
def homepage():

    # It sends top 3 competitors all mods.
    
    categories = ["Rastgele Atış","S.Rastgele Atış","Test","S.Test"]

    cursor = mysql.connection.cursor()

    execution_ratis = "SELECT username,ratis FROM users ORDER BY ratis DESC LIMIT 3"

    cursor.execute(execution_ratis)

    competitors_ratis_successful = cursor.fetchall()

    execution_sratis = "SELECT username,sratis FROM users ORDER BY sratis DESC LIMIT 3"

    cursor.execute(execution_sratis)

    competitors_sratis_successful = cursor.fetchall()

    execution_test = "SELECT username,test FROM users ORDER BY test DESC LIMIT 3"

    cursor.execute(execution_test)

    competitors_test_successful = cursor.fetchall()

    execution_stest = "SELECT username,stest FROM users ORDER BY stest DESC LIMIT 3"

    cursor.execute(execution_stest)

    competitors_stest_successful = cursor.fetchall()

    cursor.close()

    competitors_successful = {
        "Rastgele Atış": competitors_ratis_successful,
        "S.Rastgele Atış": competitors_sratis_successful,
        "Test": competitors_test_successful,
        "S.Test": competitors_stest_successful,
    }


    return render_template('homepage.html',categories=categories,competitors_successful=competitors_successful)  


@app.route("/signup",methods=["GET",'POST'])
def signup():
    if "logged_in" in session: 
        return redirect(url_for('homepage'))
    else:
        form = SignupForm(request.form)

        if request.method == 'POST' and form.validate():
            name = form.karistiran_name.data
            username = form.karistiran_username.data
            email = form.karistiran_email.data
            password = sha256_crypt.encrypt(form.karistiran_password.data)
            dil = form.karistiran_language.data

            registration = "INSERT INTO users(name, username,email,password,ratis,sratis,test,stest,dil) VALUES(%s,%s,%s,%s,0,0,0,0,%s)"

            cursor = mysql.connection.cursor()

            cursor.execute(registration,(name, username,email,password,dil))

            mysql.connection.commit()

            return redirect(url_for('homepage'))

        else:
            return render_template('signup.html',form=form)

@app.route("/login",methods=["POST", "GET"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":

        giris_username = form.giris_username.data
        giris_password = form.giris_password.data

        cursor = mysql.connection.cursor()

        _login = "SELECT * FROM users WHERE username = %s"

        result = cursor.execute(_login,(giris_username,))

        if result > 0:
            data = cursor.fetchone()
            real_password = data['password']

            if sha256_crypt.verify(giris_password,real_password):
                session['logged_in'] = True
                session['username'] = giris_username
                session['language'] = data['dil']



                return redirect(url_for('homepage'))
            else:
                return redirect(url_for('login'))
        else:
            return redirect(url_for('homepage'))
            
    else:
        return render_template('login.html',form=form)

@app.route("/logout")
def logout():
    if "logged_in" in session:
        session.clear()
        return redirect(url_for('homepage'))

@app.route("/ratis",methods=["GET","POST"])
def ratis():
    if "logged_in" in session:
        form = AnswerFrom(request.form)
        if request.method == "POST":
            #cevaplar alınıyor
            _answer = form.answer_question.data
            __answer = session["answer"]
            #yeni soru oluşturuluyor
            result = YapayZeka()
            result_txt = result[0]
            session["answer"] = result[1]
            #cevabı kontrol ediyor
            if _answer in __answer:
                _is_right = True
                #cevap kısmı boşaltılıyor
                form.answer_question.data = None
                return render_template('ratis.html',form=form,result_txt=result_txt,_is_right=_is_right)
            else:
                _is_right = False      
                #cevap kısmı boşaltılıyor
                form.answer_question.data = None     
                return render_template('ratis.html',form=form,result_txt=result_txt,_is_right=_is_right)    

        else:
            result = YapayZeka()
            result_txt = result[0]
            session["answer"] = result[1]
            return render_template('ratis.html',form=form,result_txt=result_txt)

    else:
        return redirect(url_for('homepage'))

@app.route("/sratis",methods=["GET","POST"])
def sratis():
    if "logged_in" in session:
        form = AnswerFrom(request.form)
        if request.method == "POST":
            time = request.form.get("timer")
            answer = request.form.get("answer")
            if time != "0":

                if answer in session["answer"]:
                    session["answers"][0]+=1

                result = YapayZeka()
                session["answer"] = result[1]
                session["timer"] = time
                session["answers"][1] +=1
                return render_template('sratis.html',result_txt=result)
            else:

                cursor = mysql.connection.cursor()

                send_skor = "UPDATE users SET sratis = %s WHERE username = %s"

                cursor.execute(send_skor,(session["answers"][0],session["username"]))
                
                mysql.connection.commit()

                return render_template('answer.html')
        else:
            session["timer"] = "1.00"
            result = YapayZeka()
            session["answer"] = result[1]
            # skor = 0
            session["answers"] = [0,0]
            return render_template('sratis.html',result_txt=result)

    else:
        return redirect(url_for('homepage'))

@app.route("/test",methods=["GET","POST"])
def test():
    if "logged_in" in session:
        if request.method == "POST":
            form = request.form
            #cevaplar alınıyor
            _answer = form.get("answers")
            __answer = session["answer"]
            #yeni soru oluşturuluyor
            test = YapayZekaTest()
            #global değerler
            session["answer"] = test.cevap
            #cevap kısımlarının oluşturulması
            test.answers.append(test.cevap[0])
            shuffle(test.answers)
            answers = test.answers
            txt = test.txt
            #cevabı kontrol ediyor,
            if _answer in __answer:
                _is_right = True
            else:
                _is_right = False      

            return render_template('test.html',answers=answers,txt=txt,_is_right=_is_right) 
        else:
            test = YapayZekaTest()
            #global değerler
            session["answer"] = test.cevap
            session["answers"] = [0,0]
            #cevap kısımlarının oluşturulması
            test.answers.append(test.cevap[0])
            shuffle(test.answers)
            answers = test.answers
            txt = test.txt
            return render_template('test.html',answers=answers,txt=txt)
    else:
        return redirect(url_for('homepage'))

@app.route("/stest",methods=["GET","POST"])
def stest():
    if "logged_in" in session:
        if request.method == "POST":
            
            form = request.form
            time = request.form.get("timer")
            if time != "0":

                #cevaplar alınıyor
                _answer = form.get("answers")

                if _answer in session["answer"]:
                    session["answers"][0]+=1


                #yeni soru oluşturuluyor
                test = YapayZekaTest()
                #global değerler
                session["answer"] = test.cevap
                #cevap kısımlarının oluşturulması
                test.answers.append(test.cevap[0])
                shuffle(test.answers)
                answers = test.answers
                txt = test.txt


                session["timer"] = time
                session["answers"][1] +=1
                return render_template('stest.html',answers=answers,txt=txt)
            else:
                if session["answers"] != 0:

                    cursor = mysql.connection.cursor()

                    send_skor = "UPDATE users SET stest = %s WHERE username = %s"

                    cursor.execute(send_skor,(session["answers"][0],session["username"]))
                    
                    mysql.connection.commit()

                    return render_template('answer.html')
                else:
                    session["timer"] = "1.00"
                    test = YapayZekaTest()
                    #global değerler
                    session["answer"] = test.cevap
                    session["answers"] = [0,0]
                    #cevap kısımlarının oluşturulması
                    test.answers.append(test.cevap[0])
                    shuffle(test.answers)
                    answers = test.answers
                    txt = test.txt
                    return render_template('stest.html',answers=answers,txt=txt)
                


        else:
            session["timer"] = "1.00"
            test = YapayZekaTest()
            #global değerler
            session["answer"] = test.cevap
            session["answers"] = [0,0]
            #cevap kısımlarının oluşturulması
            test.answers.append(test.cevap[0])
            shuffle(test.answers)
            answers = test.answers
            txt = test.txt
            return render_template('stest.html',answers=answers,txt=txt)
    else:
        return redirect(url_for('homepage'))

if __name__ == '__main__':
    app.run(debug=True)