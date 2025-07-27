from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = "Please enter valid numbers"
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Calculator</title>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                text-align: center; 
                padding: 50px;
                background-color: #f0f0f0;
            }}
            h1 {{ color: #333; }}
            input {{ 
                padding: 10px; 
                margin: 10px; 
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }}
            button {{ 
                padding: 10px 20px; 
                font-size: 16px; 
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }}
            button:hover {{ background-color: #0056b3; }}
            .result {{ 
                font-size: 24px; 
                color: #28a745; 
                margin-top: 20px;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form method="POST">
            <input type="number" name="num1" placeholder="Enter first number" step="any" required>
            <span style="font-size: 20px;"> + </span>
            <input type="number" name="num2" placeholder="Enter second number" step="any" required>
            <br><br>
            <button type="submit">Calculate</button>
        </form>
        
        {f'<div class="result">Result: {result}</div>' if result is not None else ''}
    </body>
    </html>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)