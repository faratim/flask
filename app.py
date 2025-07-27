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
        <script>
            function validateForm() {{
                const S = parseFloat(document.getElementById('S').value);
                const P = parseFloat(document.getElementById('P').value);
                const N = parseInt(document.getElementById('N').value);
                
                // Clear previous error messages
                clearErrors();
                
                let hasErrors = false;
                
                // Validate S
                if (isNaN(S) || S < 0) {{
                    showError('S', 'S must be a number ≥ 0');
                    hasErrors = true;
                }}
                
                // Validate P
                if (isNaN(P) || P < 0) {{
                    showError('P', 'P must be a number ≥ 0');
                    hasErrors = true;
                }}
                
                // Validate N
                if (isNaN(N) || N < 1 || N !== Math.floor(N)) {{
                    showError('N', 'N must be a positive integer');
                    hasErrors = true;
                }}
                
                return !hasErrors;
            }}
            
            function showError(fieldId, message) {{
                const field = document.getElementById(fieldId);
                field.style.borderColor = '#dc3545';
                
                const error = document.createElement('div');
                error.className = 'error-message';
                error.style.color = '#dc3545';
                error.style.fontSize = '14px';
                error.style.marginTop = '5px';
                error.textContent = message;
                
                field.parentNode.appendChild(error);
            }}
            
            function clearErrors() {{
                // Reset border colors
                document.getElementById('S').style.borderColor = '#ccc';
                document.getElementById('P').style.borderColor = '#ccc';
                document.getElementById('N').style.borderColor = '#ccc';
                
                // Remove error messages
                const errors = document.querySelectorAll('.error-message');
                errors.forEach(error => error.remove());
            }}
            
            // Real-time validation as user types
            document.addEventListener('DOMContentLoaded', function() {{
                ['S', 'P', 'N'].forEach(id => {{
                    document.getElementById(id).addEventListener('input', function() {{
                        this.style.borderColor = '#ccc';
                        const errors = this.parentNode.querySelectorAll('.error-message');
                        errors.forEach(error => error.remove());
                    }});
                }});
            }});
        </script>
    </head>
    <body>
        <h1>Calculator</h1>
        <form method="POST" onsubmit="return validateForm()">
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