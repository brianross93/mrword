# Create a Flask web app using openai GPT-3 model that can generate text for 
# a student writing an essay for school project. This Flask web app will
# show a web page to the user, and the user will be able to enter in a topic of thesis
# statement. The model will then generate an essay based off of the information
# and references given by the user. 

import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)



# Create the database model for a user to save essay in.
# This model should shave a user, the prompt/thesis they entered, and the generated essay.
class UserEssay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    prompt = db.Column(db.String(200))
    generated_essay = db.Column(db.String(200))

    def __repr__(self):
        return f"UserEssay('{self.user_id}', '{self.prompt}', '{self.generated_essay}')"


#console log the information in the database
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'UserEssay': UserEssay}


#Create the post route for the user to enter in a prompt/thesis they want to write an essay for.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['prompt']
        generated_essay = request.form['generated_essay']
        user_id = request.form['user_id']
        new_essay = UserEssay(user_id=user_id, prompt=prompt, generated_essay=generated_essay)
        db.session.add(new_essay)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('index.html')







# @app.route('/', methods= ['GET', 'POST'])
# def index():
#     if request.method == 'GET':
#         return render_template('index.html')

    
    

#     if request.method == 'POST':
#         topic = request.form['topic']
#         model_name = 'gpt2'
#         model_version = '117M'
#         # The number of characters to generate
#         num_generate = 100
#         # The temperature of the model
#         temperature = 0.7
#         # The prompt to use for the generation
#         prompt = 'The topic of the thesis is ' + topic + '.'
#         # The number of words to use for the prompt
#         length = 100
#         # The number of words to use for the response
#         max_tokens = 1000
#         # The number of top words to use for the response
#         top_p = 0.9
#         # The number of top words to use for the response
#         top_k = 0
#         # The number of top words to use for the response
#         no_cuda = False
#         # The number of top words to use for the response
#         no_sample = False
#         # The number of top words to use for the response
#         seed = 0
#         # The number of top words to use for the response
#         nsamples = 1
#         # The number of top words to use for the response
#         batch_size = 1
#         # The number of top words to use for the response
#         truncate = 0
#         # The number of top words to use for the response
#         prefix = ''
#         # The number of top words to use for the response
#         suffix = ''
#         # The number of top words to use for the response
#         gpt_tokenizer = openai.OpenaiGptTokenizer()
#         gpt_model = openai.OpenaiGptModel(model_name=model_name, model_version=model_version,
#                                           tokenizer=gpt_tokenizer)
#         # Generate the text
#         generated = gpt_model.generate(
#             prompt=prompt,
#             num_generate=num_generate,
#             temperature=temperature,
#             top_p=top_p,
#             top_k=top_k,
#             no_cuda=no_cuda,
#             no_sample=no_sample,
#             seed=
#             seed,
#             nsamples=nsamples,
#             batch_size=batch_size,
#             truncate=truncate,
#             prefix=prefix,
#             suffix=suffix)
#         # Save the generated essay to the database
#         essay = UserEssay(user_id=1, prompt=prompt, generated_essay=generated)
#         db.session.add(essay)
#         db.session.commit()
#         return render_template('index.html', generated=generated)

    return render_template('index.html')



    



