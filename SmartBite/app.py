from flask import Flask, request, render_template_string

app = Flask(__name__)

# Local food database
FOOD_DATABASE = {
    "pizza": {
        "description": "Pizza is a beloved Italian dish featuring a thin or thick crust topped with tomato sauce, cheese, and various toppings. It's known for its versatility and can be enjoyed with countless flavor combinations.",
        "ingredients": ["Flour", "Yeast", "Salt", "Water", "Tomato sauce", "Mozzarella cheese", "Olive oil", "Toppings of choice"],
        "nutrition": {"calories": 285, "carbs": 36, "fat": 10, "protein": 12}
    },
    "biryani": {
        "description": "Biryani is a fragrant Indian rice dish cooked with spices, meat or vegetables, and basmati rice. It's a complete meal known for its aromatic and flavorful layers of rice and protein.",
        "ingredients": ["Basmati rice", "Meat or vegetables", "Yogurt", "Ginger-garlic paste", "Onions", "Spices (cumin, cinnamon, bay leaf)", "Ghee", "Saffron"],
        "nutrition": {"calories": 320, "carbs": 45, "fat": 12, "protein": 18}
    },
    "biriyani": {
        "description": "Biryani is a fragrant Indian rice dish cooked with spices, meat or vegetables, and basmati rice. It's a complete meal known for its aromatic and flavorful layers of rice and protein.",
        "ingredients": ["Basmati rice", "Meat or vegetables", "Yogurt", "Ginger-garlic paste", "Onions", "Spices (cumin, cinnamon, bay leaf)", "Ghee", "Saffron"],
        "nutrition": {"calories": 320, "carbs": 45, "fat": 12, "protein": 18}
    },
    "sushi": {
        "description": "Sushi is a Japanese delicacy made with seasoned rice, fresh fish, vegetables, and nori (seaweed). It's an elegant dish known for its fresh flavors and artful presentation.",
        "ingredients": ["Sushi rice", "Nori (seaweed)", "Fresh fish", "Vegetables (cucumber, avocado)", "Wasabi", "Soy sauce", "Vinegar"],
        "nutrition": {"calories": 140, "carbs": 20, "fat": 3, "protein": 15}
    },
    "dosa": {
        "description": "Dosa is a South Indian crepe made from fermented rice and lentil batter. It's crispy on the outside and soft inside, typically served with sambar and chutney.",
        "ingredients": ["Rice", "Lentils", "Salt", "Oil", "Spices", "Optional fillings (potato, paneer)"],
        "nutrition": {"calories": 180, "carbs": 28, "fat": 5, "protein": 6}
    },
    "chicken curry": {
        "description": "Chicken curry is a savory dish featuring tender chicken pieces cooked in a rich, spiced gravy. It's a comfort food staple in many cuisines across Asia.",
        "ingredients": ["Chicken", "Onions", "Tomatoes", "Coconut milk or yogurt", "Spices (cumin, turmeric, chili)", "Garlic", "Ginger"],
        "nutrition": {"calories": 280, "carbs": 8, "fat": 16, "protein": 28}
    },
    "pasta": {
        "description": "Pasta is an Italian staple made from wheat flour dough, available in countless shapes. It's typically served with sauces ranging from simple tomato to creamy and meat-based.",
        "ingredients": ["Wheat flour", "Eggs", "Salt", "Water", "Sauce ingredients vary"],
        "nutrition": {"calories": 220, "carbs": 40, "fat": 2, "protein": 8}
    }
}

def fetch_food_info(food_item):
    # Search for the food item (case-insensitive)
    food_lower = food_item.lower().strip()
    
    # Direct match
    if food_lower in FOOD_DATABASE:
        food_data = FOOD_DATABASE[food_lower]
    else:
        # Partial match
        for key in FOOD_DATABASE:
            if key in food_lower or food_lower in key:
                food_data = FOOD_DATABASE[key]
                food_item = key.title()
                break
        else:
            # Default response if not found
            return f"""<strong>Description:</strong> {food_item.title()} is a delicious dish with unique flavors and cultural significance.

<strong>Ingredients:</strong>
- Ingredient 1
- Ingredient 2
- Ingredient 3
- Ingredient 4

<strong>Nutrition (per serving):</strong>
- Calories: 250
- Carbohydrates: 30g
- Fat: 10g
- Protein: 15g

<strong>Recipe Videos:</strong>
<a href="https://www.youtube.com/results?search_query={food_item} recipe english" target="_blank">English Recipe</a>
<a href="https://www.youtube.com/results?search_query={food_item} recipe malayalam" target="_blank">Malayalam Recipe</a>"""
    
    # Format the response
    ingredients_list = "\n".join([f"- {ing}" for ing in food_data["ingredients"]])
    nutrition = food_data["nutrition"]
    
    response = f"""<strong>Description:</strong> {food_data['description']}

<strong>Ingredients:</strong>
{ingredients_list}

<strong>Nutrition (per serving):</strong>
- Calories: {nutrition['calories']}
- Carbohydrates: {nutrition['carbs']}g
- Fat: {nutrition['fat']}g
- Protein: {nutrition['protein']}g

<strong>Recipe Videos:</strong>
<a href="https://www.youtube.com/results?search_query={food_item} recipe english" target="_blank">English Recipe</a>
<a href="https://www.youtube.com/results?search_query={food_item} recipe malayalam" target="_blank">Malayalam Recipe</a>"""
    
    
    return response

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SmartBite - Your Smart Food Assistant</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; }
    h1, h2, h3 { font-family: 'Playfair Display', serif; }
    .markdown-content h1, .markdown-content h2, .markdown-content h3 {
      font-family: 'Playfair Display', serif; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #1f2937;
    }
    .markdown-content p { margin-bottom: 1rem; line-height: 1.6; }
    .markdown-content ul { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1rem; }
    .markdown-content li { margin-bottom: 0.25rem; }
    .markdown-content strong { color: #111827; }
  </style>
</head>
<body class="bg-stone-50 text-stone-900">
  <div class="min-h-screen bg-stone-50 pb-20">
    <header class="pt-20 pb-16 px-6">
      <div class="max-w-4xl mx-auto text-center">
        <div class="inline-block bg-amber-100 text-amber-800 px-4 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider mb-6">
          Bilingual AI Assistant
        </div>
        <h1 class="text-6xl md:text-7xl font-bold text-stone-900 mb-6 tracking-tight">
          Smart<span class="text-amber-600">Bite</span>
        </h1>
        <p class="text-xl md:text-2xl text-stone-500 font-light max-w-2xl mx-auto">
          Actionable food insights in English and Malayalam.
        </p>
      </div>
    </header>
    <main class="max-w-4xl mx-auto px-6">
      <div class="sticky top-8 z-50 mb-16">
        <form method="get" class="w-full max-w-2xl mx-auto">
          <div class="relative group">
            <input type="text" name="query" placeholder="Enter a food item (e.g., Pizza, Biryani, Sushi)"
              class="w-full px-6 py-5 text-lg bg-white border border-stone-200 rounded-3xl shadow-sm focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-transparent transition-all placeholder:text-stone-400 group-hover:shadow-md" value="{{ query }}" />
            <button type="submit" class="absolute right-3 top-3 bottom-3 px-6 rounded-2xl font-semibold transition-all flex items-center justify-center bg-stone-900 text-white hover:bg-stone-800">
              Ask SmartBite
            </button>
          </div>
        </form>
      </div>
      <div class="space-y-12">
        {% if result %}
        <div class="bg-gradient-to-br from-amber-50 via-white to-orange-50 rounded-[2.5rem] p-8 border-2 border-amber-200 shadow-2xl mb-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
          <div class="flex justify-between items-start mb-8 border-b-2 border-amber-100 pb-6">
            <div>
              <h2 class="text-5xl md:text-6xl text-transparent bg-clip-text bg-gradient-to-r from-amber-600 to-orange-600 font-bold mb-2 capitalize">{{ query }}</h2>
              <div class="flex items-center space-x-2">
                <span class="inline-block w-2 h-2 bg-gradient-to-r from-amber-500 to-orange-500 rounded-full"></span>
                <span class="text-amber-700 text-sm font-bold uppercase tracking-widest">Smart Analysis</span>
              </div>
            </div>
            <div class="bg-gradient-to-r from-amber-400 to-orange-400 text-white px-6 py-3 rounded-full text-sm font-bold flex items-center shadow-lg transform hover:scale-105 transition-transform">
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1a1 1 0 112 0v1a1 1 0 11-2 0zM13.536 14.95a1 1 0 010-1.414l.707-.707a1 1 0 011.414 1.414l-.707.707a1 1 0 01-1.414 0zM6.464 14.95a1 1 0 01-1.414 0l-.707-.707a1 1 0 011.414-1.414l.707.707a1 1 0 010 1.414z" />
              </svg>
              AI Powered
            </div>
          </div>
          <div class="markdown-content prose prose-stone max-w-none text-stone-700 space-y-4">
            <style>
              .markdown-content { font-size: 1.05rem; line-height: 1.8; }
              .markdown-content strong { color: #b45309; font-weight: 700; display: block; margin-top: 1.5rem; margin-bottom: 0.75rem; font-size: 1.2rem; }
              .markdown-content strong:first-child { margin-top: 0; }
              .markdown-content h2 { color: #d97706; font-size: 1.5rem; font-weight: 700; margin-top: 1.5rem; margin-bottom: 1rem; }
              .markdown-content ul { 
                background: linear-gradient(135deg, rgba(251,191,36,0.1) 0%, rgba(249,115,22,0.1) 100%); 
                padding: 1.5rem; 
                border-radius: 1rem; 
                border-left: 4px solid #f59e0b; 
                margin: 1rem 0;
                list-style-position: inside;
              }
              .markdown-content li { 
                color: #78350f; 
                margin: 0.75rem 0; 
                line-height: 1.6;
              }
              .markdown-content a { 
                display: inline-block;
                background: linear-gradient(135deg, #f59e0b 0%, #f97316 100%);
                color: white;
                padding: 0.75rem 1.5rem;
                border-radius: 0.75rem;
                font-weight: 600;
                text-decoration: none;
                margin: 0.5rem 0.5rem 0.5rem 0;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(245, 158, 11, 0.3);
              }
              .markdown-content a:hover {
                transform: translateY(-2px);
                box-shadow: 0 6px 12px rgba(245, 158, 11, 0.4);
                background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
              }
              .markdown-content br { margin: 0.5rem 0; }
            </style>
            {{ result | safe }}
          </div>
        </div>
        {% else %}
        <div class="text-center py-32 bg-gradient-to-br from-amber-50 to-orange-50 rounded-[2.5rem] border-2 border-dashed border-amber-200 shadow-lg hover:shadow-xl transition-shadow">
          <div class="text-amber-200 mb-8 animate-bounce">
            <svg class="w-24 h-24 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <h3 class="text-3xl font-bold bg-gradient-to-r from-amber-600 to-orange-600 text-transparent bg-clip-text">Discover Something Tasty</h3>
          <p class="text-amber-700 mt-4 text-lg font-medium">Enter any food name to get detailed bilingual guides.</p>
          <div class="mt-8 flex justify-center space-x-2">
            <div class="w-2 h-2 bg-amber-500 rounded-full animate-pulse"></div>
            <div class="w-2 h-2 bg-orange-500 rounded-full animate-pulse" style="animation-delay: 0.2s"></div>
            <div class="w-2 h-2 bg-amber-400 rounded-full animate-pulse" style="animation-delay: 0.4s"></div>
          </div>
        </div>
        {% endif %}
      </div>
    </main>
    <footer class="mt-24 py-12 border-t border-stone-100 text-center text-stone-400">
      <p class="text-sm font-medium tracking-wide">SMARTBITE &copy; 2026</p>
      <p class="text-xs mt-1">Powered by Local Food Database</p>
    </footer>
  </div>
</body>
</html>
"""
@app.route('/', methods=['GET', 'POST'])
def index():
    query = ""
    result = ""
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
    elif request.method == 'GET':
        query = request.args.get('query', '').strip()
    if query:
        result = fetch_food_info(query)
    return render_template_string(HTML_TEMPLATE, query=query, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)