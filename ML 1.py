class RecommendationSystem:
    def __init__(self, user_data, threshold):
        self.user_data = user_data
        self.threshold = threshold

    def calculate_repeated_plays(self):
        recommendations = []
        for song, days in self.user_data.items():
            if len(days) >= self.threshold:
                recommendations.append(song)
        return recommendations

    def get_recommendations(self):
        recommendations = self.calculate_repeated_plays()
        return recommendations

if __name__ == "__main__":

    user_data = {
        'song1': [1, 5, 10, 20],
        'song2': [2, 18],
        'song3': [3, 4, 5, 6, 7, 8],
        'song4': [15],
        'song5': [14, 28] 
    }


    threshold = 3

    rec_system = RecommendationSystem(user_data, threshold)

    recommended_songs = rec_system.get_recommendations()

    print("Recommended Songs:", recommended_songs)
