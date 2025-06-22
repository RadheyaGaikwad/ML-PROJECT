from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            form = request.form.to_dict()
            reading = form.get('reading_score')
            writing = form.get('writing_score')

            if not (reading and writing):
                return "<h3 style='color:red;'>Please fill both Reading and Writing scores.</h3>"

            data = CustomData(
                gender=form.get('gender'),
                race_ethnicity=form.get('ethnicity'),
                parental_level_of_education=form.get('parental_level_of_education'),
                lunch=form.get('lunch'),
                test_preparation_course=form.get('test_preparation_course'),
                reading_score=float(reading),
                writing_score=float(writing)
            )

            pred_df = data.get_data_as_dataframe()
            results = PredictPipeline().predict(pred_df)

            return render_template('home.html', results=results[0])

        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"<h3 style='color:red;'>Error occurred: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
