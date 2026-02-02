
from flask import Flask, render_template, request, jsonify
from homoglyphs import generate_variants

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    word = data.get('word', '')
    
    if not word:
        return jsonify({'error': 'No word provided'}), 400
        
    # Cap input length for safety
    if len(word) > 50:
         return jsonify({'error': 'Word too long (max 50 chars)'}), 400

    variants, total_count = generate_variants(word)
    
    return jsonify({
        'original': word,
        'count': len(variants),
        'total_possible': total_count,
        'variants': variants
    })

if __name__ == '__main__':
    # Run localhost
    app.run(debug=True, port=5000)
