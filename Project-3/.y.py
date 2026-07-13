

print("===== AI Recommendation System =====")

# Data
recommendations = {
    "action": ["Avengers", "John Wick", "Mission Impossible"],
    "comedy": ["Friends", "Mr. Bean", "The Office"],
    "horror": ["The Conjuring", "Annabelle", "IT"],
    "technology": ["Python Course", "AI Basics", "Machine Learning"],
    "sports": ["Football Highlights", "Cricket World Cup", "Olympics"]
}

# User Input
choice = input("Enter your interest (Action/Comedy/Horror/Technology/Sports): ").lower()

# Recommendation Logic
if choice in recommendations:
    print("\nRecommended for you:")
    for item in recommendations[choice]:
        print("-", item)
else:
    print("\nSorry! No recommendations found.")