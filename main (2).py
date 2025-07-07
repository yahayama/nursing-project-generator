from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Nursing Project Topic Generator</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
        .container { max-width: 700px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #333; }
        label { display: block; margin-top: 15px; font-weight: bold; }
        input, select { width: 100%; padding: 10px; margin-top: 5px; border-radius: 4px; border: 1px solid #ccc; }
        button { margin-top: 20px; padding: 10px 20px; background: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 30px; background: #e9f7ef; padding: 15px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Nursing Project Topic Generator</h1>
        <form method="post">
            <label>Area of Interest:</label>
            <select name="interest" required>
                <option>Pediatrics</option>
                <option>Maternal Health</option>
                <option>Mental Health</option>
                <option>Community Health</option>
                <option>Medical-Surgical</option>
            </select>

            <label>Who is your target population?</label>
            <input type="text" name="population" placeholder="e.g. Nursing students at ABU Zaria" required>

            <label>Study Setting:</label>
            <input type="text" name="setting" placeholder="e.g. ABUTH Zaria" required>

            <label>Specific Focus Area (optional):</label>
            <input type="text" name="focus" placeholder="e.g. Malnutrition, Hand hygiene, etc.">

            <button type="submit">Generate Topics</button>
        </form>

        {% if topics %}
        <div class="result">
            <h3>Suggested Project Topics:</h3>
            <ul>
                {% for topic in topics %}
                <li>{{ topic }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
'''

def generate_topics(interest, population, setting, focus):
    base = f"in {setting}"
    focus_phrase = f" on {focus}" if focus else ""
    topics = []

    if interest == "Pediatrics":
        topics.append(f"Assessment of caregivers' knowledge{focus_phrase} among pediatric patients' relatives {base}")
        topics.append(f"Impact of health education on caregivers’ practices towards child care{focus_phrase} {base}")
        topics.append(f"Prevalence of common pediatric health conditions and caregivers' response{focus_phrase} {base}")
    elif interest == "Maternal Health":
        topics.append(f"Knowledge and practice of exclusive breastfeeding among mothers attending antenatal clinic {base}")
        topics.append(f"Effect of health education on postpartum care practices{focus_phrase} {base}")
        topics.append(f"Assessment of mothers’ attitudes towards family planning methods {base}")
    elif interest == "Mental Health":
        topics.append(f"Perception of mental illness and help-seeking behavior among {population} {base}")
        topics.append(f"Assessment of stress management techniques among student nurses{focus_phrase} {base}")
        topics.append(f"Knowledge and attitude of nurses towards patients with mental health disorders {base}")
    elif interest == "Community Health":
        topics.append(f"Community awareness and preventive practices{focus_phrase} among {population} {base}")
        topics.append(f"Role of community health nurses in promoting sanitation and hygiene {base}")
        topics.append(f"Assessment of immunization practices among mothers in selected communities {base}")
    elif interest == "Medical-Surgical":
        topics.append(f"Knowledge and practice of infection prevention among nurses{focus_phrase} {base}")
        topics.append(f"Assessment of postoperative care among surgical patients in {setting}")
        topics.append(f"Effect of health education on pain management practices among nurses {base}")

    return topics

@app.route('/', methods=['GET', 'POST'])
def home():
    topics = []
    if request.method == 'POST':
        interest = request.form['interest']
        population = request.form['population']
        setting = request.form['setting']
        focus = request.form['focus']
        topics = generate_topics(interest, population, setting, focus)
    return render_template_string(html_template, topics=topics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
