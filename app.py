from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    
    if request.method == 'POST':
        try:
            S = float(request.form['S'])
            P = float(request.form['P'])
            N = int(request.form['N'])
            Omega = request.form.get('Omega') == '1'
            
            # Your calculation logic will go here
            result = f"S={S}, P={P}, N={N}, Omega={'Bounded' if Omega else 'Unbounded'}"
            
        except ValueError:
            result = "Please enter valid inputs"
    
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator</title>
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                text-align: center; 
                padding: 50px;
                background-color: #f0f0f0;
            }}
            h1 {{ color: #333; }}
            .input-group {{
                margin: 15px 0;
                text-align: left;
                display: inline-block;
            }}
            label {{
                display: inline-block;
                width: 120px;
                font-weight: bold;
            }}
            input, select {{ 
                padding: 8px; 
                margin: 5px; 
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                width: 200px;
            }}
            button {{ 
                padding: 12px 24px; 
                font-size: 16px; 
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                margin-top: 20px;
            }}
            button:hover {{ background-color: #0056b3; }}
            .result {{ 
                font-size: 18px; 
                color: #28a745; 
                margin-top: 20px;
                font-weight: bold;
                padding: 15px;
                background-color: white;
                border-radius: 5px;
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <h1>Calculator</h1>
        <form method="POST">
            <div class="input-group">
                <label for="S">S (≥ 0):</label>
                <input type="number" name="S" id="S" step="any" min="0" placeholder="Enter S value" required>
            </div>
            <br>
            
            <div class="input-group">
                <label for="P">P (≥ 0):</label>
                <input type="number" name="P" id="P" step="any" min="0" placeholder="Enter P value" required>
            </div>
            <br>
            
            <div class="input-group">
                <label for="N">N (> 0):</label>
                <input type="number" name="N" id="N" min="1" step="1" placeholder="Enter N value" required>
            </div>
            <br>
            
            <div class="input-group">
                <label for="Omega">Omega:</label>
                <select name="Omega" id="Omega">
                    <option value="1" selected>Bounded</option>
                    <option value="0">Unbounded</option>
                </select>
            </div>
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