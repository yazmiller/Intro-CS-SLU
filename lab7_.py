# -*- coding: utf-8 -*-
"""lab7 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/158KMu_yJBKJ-VboaxOPVUETkoUXGVhUX
"""

<html>
    <body>
            <h1> CSCI1020: Build in-class Genomics %G~C Content Calculator </h1>
            <h1> Yazmin Miller </h1>
            <div>
            This is a tool which allows the calculation of the Genomics %G~C Content in a nucleotide (DNA) sequence.
            <br>
            Reference: <a href="https://www.sciencebuddies.org/science-fair-projects/references/genomics-g-c-content-calculator" target="_blank">Official Online tool</a>
            </div>

            <h2>Upload your DNA sequence:</h2>

            <form method="POST" enctype="multipart/form-data">
                <p><textarea name="dna_seq" cols="100" rows="5"></textarea></p>
                <input type="submit" value="Calculate" style = "font-size:30px">
            </form>

            <hr>

            <h1>Results:</h1>
            <h2>Submitted DNA Sequence:</h2>

            <p><textarea name="dna_seq" cols="100" rows="5"> ACGGACGGTT </textarea></p>

            <h2>Results of Calculation:</h2>
            <p>Total count, all bases: <textarea cols="50" rows="1">{{ n_bp }}</textarea></p>
            <p>Adenine (A) count: <textarea cols="50" rows="1">{{ n_A }}</textarea></p>
            <p>Thymine (T) count: <textarea cols="50" rows="1">{{ n_T }}</textarea></p>
            <p>Guanine (G) count: <textarea cols="50" rows="1">{{ n_G }}</textarea></p>
            <p>Cytosine (C) count: <textarea cols="50" rows="1">{{ n_C }}</textarea></p>
            <p>%G~C content: <textarea cols="50" rows="1">{{ GC }}</textarea></p>

            {% endif %}
    </body>
</html>

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# Code cell <4GteEzu7Sd-9>
# #%% [code]
# '''
# The following codes are used to bring your codes to webpage so that you are able to submit your sequence through website to perform computational task.
# '''
# 
# ##### web application packages
# !pip install flask-ngrok
# from flask_ngrok import run_with_ngrok
# from flask import Flask, request, render_template
# ! mkdir templates
# Execution output
# 2KB
# 	Stream
# 		Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
# 		Requirement already satisfied: flask-ngrok in /usr/local/lib/python3.7/dist-packages (0.0.25)
# 		Requirement already satisfied: Flask>=0.8 in /usr/local/lib/python3.7/dist-packages (from flask-ngrok) (1.1.4)
# 		Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (from flask-ngrok) (2.23.0)
# 		Requirement already satisfied: itsdangerous<2.0,>=0.24 in /usr/local/lib/python3.7/dist-packages (from Flask>=0.8->flask-ngrok) (1.1.0)
# 		Requirement already satisfied: click<8.0,>=5.1 in /usr/local/lib/python3.7/dist-packages (from Flask>=0.8->flask-ngrok) (7.1.2)
# 		Requirement already satisfied: Werkzeug<2.0,>=0.15 in /usr/local/lib/python3.7/dist-packages (from Flask>=0.8->flask-ngrok) (1.0.1)
# 		Requirement already satisfied: Jinja2<3.0,>=2.10.1 in /usr/local/lib/python3.7/dist-packages (from Flask>=0.8->flask-ngrok) (2.11.3)
# 		Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from Jinja2<3.0,>=2.10.1->Flask>=0.8->flask-ngrok) (2.0.1)
# 		Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests->flask-ngrok) (1.24.3)
# 		Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests->flask-ngrok) (3.0.4)
# 		Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests->flask-ngrok) (2022.9.24)
# 		Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests->flask-ngrok) (2.10)
# 		mkdir: cannot create directory ‘templates’: File exists
# 
# Code cell <NlvONQ2gskwU>
# #%% [code]
# from flask import Flask, request, render_template
# 
# Code cell <fYtmmkQoTOZ1>
# #%% [code]
# !ls
# Execution output
# 0KB
# 	Stream
# 		sample_data
# 
# Code cell <HafR2R6ssuhC>
# #%% [code]
# ! mkdir templates
# !ls
# Execution output
# 0KB
# 	Stream
# 		mkdir: cannot create directory ‘templates’: File exists
# 		sample_data  templates
# 
# Code cell <DD6n8dN0UKHn>
# #%% [code]
# ######  Write webpage for front-end visualization
# %%writefile templates/index.html
# <html>
#     <body>
#             <h1> CSCI1020: Build in-class Genomics %G~C Content Calculator </h1>
#             <h1> Tae-Hyuk (Ted) Ahn </h1>
#             <div>
#             This is a tool which allows the calculation of the Genomics %G~C Content in a nucleotide (DNA) sequence.
#             <br>
#             Reference: <a href="https://www.sciencebuddies.org/science-fair-projects/references/genomics-g-c-content-calculator" target="_blank">Official Online tool</a>
#             </div>
# 
#             <h2>Upload your DNA sequence:</h2>
# 
#             <form method="POST" enctype="multipart/form-data">
#                 <p><textarea name="dna_seq" cols="100" rows="5"></textarea></p>
#                 <input type="submit" value="Calculate" style = "font-size:30px">
#             </form>
# 
#             <hr>
# 
#             {% if dna_seq %}
#             <h1>Results:</h1>
#             <h2>Submitted DNA Sequence:</h2>
# 
#             <p><textarea name="dna_seq" cols="100" rows="5">{{ dna_seq }}</textarea></p>
# 
#             <h2>Results of Calculation:</h2>
#             <p>Total count, all bases: <textarea cols="50" rows="1">{{ n_bp }}</textarea></p>
#             <p>Adenine (A) count: <textarea cols="50" rows="1">{{ n_A }}</textarea></p>
#             <p>Thymine (T) count: <textarea cols="50" rows="1">{{ n_T }}</textarea></p>
#             <p>Guanine (G) count: <textarea cols="50" rows="1">{{ n_G }}</textarea></p>
#             <p>Cytosine (C) count: <textarea cols="50" rows="1">{{ n_C }}</textarea></p>
#             <p>%G~C content: <textarea cols="50" rows="1">{{ GC }}</textarea></p>
# 
#             {% endif %}
#     </body>
# </html>
# Execution output
# 0KB
# 	Stream
# 		Overwriting templates/index.html
# 
# Code cell <7lWmy18jV55m>
# #%% [code]
# def get_GC_content(DNA):
#   DNA_G = DNA.count('G')
#   DNA_C = DNA.count('C')
#   DNA_A = DNA.count('A')
#   DNA_T = DNA.count('T')
#   GC_Content = (DNA_G + DNA_C)/(DNA_A + DNA_T + DNA_G + DNA_C) * 100
#   return GC_Content
# 
# Code cell <YIZO5FqZf_2_>
# #%% [code]
# from google.colab.output import eval_js
# print(eval_js("google.colab.kernel.proxyPort(5000)"))
# Execution output
# 0KB
# 	Stream
# 		https://o33awbpz1m-496ff2e9c6d22116-5000-colab.googleusercontent.com/
# 
# Code cell <cNKiMZtqtHgC>
# #%% [code]
# from flask import Flask
# app = Flask(__name__)
# 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# 
# app.run()
# Execution output
# 1KB
# 	Stream
# 		* Serving Flask app "__main__" (lazy loading)
# 		 * Environment: production
# 		[31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
# 		[2m   Use a production WSGI server instead.[0m
# 		 * Debug mode: off
# 		INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 16:12:25] "[37mGET / HTTP/1.1[0m" 200 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 16:12:26] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
# 
# Code cell <LbBHMA-atcYd>
# #%% [code]
# from google.colab.output import eval_js
# print(eval_js("google.colab.kernel.proxyPort(5000)"))
# Execution output
# 0KB
# 	Stream
# 		https://o33awbpz1m-496ff2e9c6d22116-5000-colab.googleusercontent.com/
# 
# Code cell <Rq2MTC0eVtI9>
# #%% [code]
# app = Flask(__name__)
# 
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         dna_seq = request.form['dna_seq']
#         dna_seq = dna_seq.replace('\n', '').replace('\r', '').replace(' ', '')
# 
#         '''
#         Call the function to perform GC content calculation
#         '''
# 
#         #GC = get_GC_content(dna_seq)
# 
#         n_bp = len(dna_seq)
#         n_A = dna_seq.count('A')
#         n_T = dna_seq.count('T')
#         n_C = dna_seq.count('C')
#         n_G = dna_seq.count('G')
#         GC_content = (n_G+n_C)/(n_A + n_T + n_G + n_C)*100
# 
#         return render_template('index.html',
#                                dna_seq=dna_seq,
#                                GC=GC_content,
#                                n_bp=n_bp,
#                                n_A=n_A,
#                                n_T=n_T,
#                                n_C=n_C,
#                                n_G=n_G)
#     else:
#         return render_template('index.html')
# app.run()
# Execution output
# 1KB
# 	Stream
# 		* Serving Flask app "__main__" (lazy loading)
# 		 * Environment: production
# 		[31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
# 		[2m   Use a production WSGI server instead.[0m
# 		 * Debug mode: off
# 		INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 16:12:38] "[37mGET / HTTP/1.1[0m" 200 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 16:12:38] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 16:13:12] "[37mPOST / HTTP/1.1[0m" 200 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 16:13:13] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
# 
# Code cell <8sF0sdO4erQy>
# #%% [code]
# from google.colab.output import eval_js
# print(eval_js("google.colab.kernel.proxyPort(5000)"))
# Execution output
# 0KB
# 	Stream
# 		https://6lx3iuheyiu-496ff2e9c6d22116-5000-colab.googleusercontent.com/
# 
# Code cell <MJp4yCtJe4sp>
# #%% [code]
# from flask import Flask, render_template, request
# app = Flask(__name__)
# 
# @app.route("/")
# def home():
#     return "Hello World"
# 
# if __name__ == "__main__":
#     app.run()
# Execution output
# 1KB
# 	Stream
# 		* Serving Flask app "__main__" (lazy loading)
# 		 * Environment: production
# 		[31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
# 		[2m   Use a production WSGI server instead.[0m
# 		 * Debug mode: off
# 		INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 15:10:12] "[37mGET / HTTP/1.1[0m" 200 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 15:10:12] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 15:10:21] "[37mGET / HTTP/1.1[0m" 200 -
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 15:10:21] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
# 
# Code cell <xyGeallWZgIc>
# #%% [code]
# from flask_ngrok import run_with_ngrok
# from flask import Flask
# app = Flask(__name__)
# run_with_ngrok(app)
# 
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
# 
# app.run()
# Execution output
# 1KB
# 	Stream
# 		* Serving Flask app "__main__" (lazy loading)
# 		 * Environment: production
# 		[31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
# 		[2m   Use a production WSGI server instead.[0m
# 		 * Debug mode: off
# 		INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 		* Running on http://d7e5-35-185-97-221.ngrok.io
# 		 * Traffic stats available on http://127.0.0.1:4040
# 
# Code cell <YFmJkm-1bVfB>
# #%% [code]
# from flask import Flask
# from flask_ngrok import run_with_ngrok
# app = Flask(__name__)
# run_with_ngrok(app)
# 
# @app.route("/")
# def home():
#     return "<h1>GFG is great platform to learn</h1>"
# 
# app.run()
# Execution output
# 1KB
# 	Stream
# 		* Serving Flask app "__main__" (lazy loading)
# 		 * Environment: production
# 		[31m   WARNING: This is a development server. Do not use it in a production deployment.[0m
# 		[2m   Use a production WSGI server instead.[0m
# 		 * Debug mode: off
# 		INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 		* Running on http://7670-35-185-97-221.ngrok.io
# 		 * Traffic stats available on http://127.0.0.1:4040
# 		INFO:werkzeug:127.0.0.1 - - [17/Oct/2022 14:59:19] "[37mGET / HTTP/1.1[0m" 200 -