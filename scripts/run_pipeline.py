from app.services.pipeline import SentimentPipeline

pipeline = SentimentPipeline()

results = pipeline.run(max_results=10)

output_file = pipeline.save_results(results)

print(f"\nResults saved to: {output_file}\n")

for result in results:
    print("-" * 60)
    print("Tweet:", result["text"])
    print("Sentiment:", result["sentiment"])
    print("Polarity:", round(result["polarity"], 3))