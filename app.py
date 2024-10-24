from flask import Flask, render_template, jsonify
import json
import random
import os

app = Flask(__name__)

# 질문 로드
def load_questions():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'questions.json')
        print(f"Attempting to load questions from: {file_path}")
        
        if not os.path.exists(file_path):
            print(f"Error: File not found at {file_path}")
            return []
        
        with open(file_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        
        print(f"Successfully loaded {len(questions)} questions")
        return questions
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []
    except Exception as e:
        print(f"Error loading questions: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    questions = load_questions()
    print("Loaded questions:", questions)  # 서버 콘솔에 로드된 질문을 출력
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
