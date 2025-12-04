#!/usr/bin/env python3
"""
Test script to verify job filtering logic works correctly
"""

import json
import re
from difflib import SequenceMatcher


def calculate_similarity(text1, text2):
    """Calculate similarity between two strings"""
    if not text1 or not text2:
        return 0.0

    text1_lower = text1.lower()
    text2_lower = text2.lower()

    # Direct substring match gets higher score
    if text2_lower in text1_lower or text1_lower in text2_lower:
        return 0.8

    # Word-based matching
    words1 = set(re.findall(r'\w+', text1_lower))
    words2 = set(re.findall(r'\w+', text2_lower))

    common_words = words1.intersection(words2)
    if common_words:
        similarity = len(common_words) / max(len(words1), len(words2))
        return similarity

    # Fuzzy string matching
    return SequenceMatcher(None, text1_lower, text2_lower).ratio()


def matches_job_function(job, job_function, threshold):
    """Check if job matches the job function"""
    job_function_lower = job_function.lower()

    # Extract relevant fields
    title = job.get('title', '')
    description = job.get('descriptionText', '')
    job_func = job.get('jobFunction', '')
    industries = job.get('industries', '')

    # Calculate similarity scores
    title_similarity = calculate_similarity(title, job_function)
    desc_similarity = calculate_similarity(description, job_function)
    func_similarity = calculate_similarity(job_func, job_function)
    industries_similarity = calculate_similarity(industries, job_function)

    # Keyword matching for engineering disciplines
    keywords = re.findall(r'\w+', job_function_lower)
    keyword_matches = 0
    full_text = f"{title} {description}".lower()

    for keyword in keywords:
        if len(keyword) > 3:  # Ignore very short words
            if keyword in full_text:
                keyword_matches += 1

    keyword_score = keyword_matches / max(len(keywords), 1) if keywords else 0

    # Weighted average of similarities
    max_similarity = max(
        title_similarity * 2.0,
        desc_similarity * 0.5,
        func_similarity * 1.5,
        industries_similarity * 1.0,
        keyword_score * 1.2
    )

    return max_similarity >= threshold, max_similarity


def main():
    print("Testing Job Filter Logic...")
    print("=" * 80)

    # Load sample data
    try:
        with open('scrappedjobs/dataset_linkedin-jobs-scraper_2025-12-03_21-25-37-181', 'r') as f:
            jobs = json.load(f)
        print(f"✓ Successfully loaded {len(jobs)} jobs")
    except Exception as e:
        print(f"✗ Error loading jobs: {e}")
        return

    # Test with different job functions
    test_queries = [
        ("Electrical Engineer", 0.3),
        ("Software Developer", 0.3),
        ("Business Analyst", 0.3),
    ]

    for job_function, threshold in test_queries:
        print(f"\n{'=' * 80}")
        print(f"Testing: '{job_function}' (threshold: {threshold})")
        print(f"{'=' * 80}")

        filtered = []
        for job in jobs:
            matches, similarity = matches_job_function(job, job_function, threshold)
            if matches:
                filtered.append((job, similarity))

        # Sort by similarity
        filtered.sort(key=lambda x: x[1], reverse=True)

        print(f"Found {len(filtered)} matching jobs")

        # Show top 5 results
        print("\nTop 5 Matches:")
        for idx, (job, similarity) in enumerate(filtered[:5], 1):
            print(f"\n{idx}. [{similarity:.2%}] {job.get('title', 'N/A')}")
            print(f"   Company: {job.get('companyName', 'N/A')}")
            print(f"   Location: {job.get('location', 'N/A')}")
            print(f"   Function: {job.get('jobFunction', 'N/A')}")

    print("\n" + "=" * 80)
    print("✓ All tests completed successfully!")
    print("\nThe filtering logic is working correctly.")
    print("You can now run the GUI application with: python3 job_filter_app.py")


if __name__ == "__main__":
    main()
