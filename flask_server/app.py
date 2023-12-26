from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])

def recommend_places():
    try:
        data = request.get_jsonq()
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        recommend_places = process_recommend(latitude, longitude)
        return jsonify({'recommend_places': recommend_places})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def process_recommend(latitude, longitude):
    return ['Place1','Place2','Place3']

if __name__ == '__main__':
    app.run(debug=True)