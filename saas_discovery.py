#!/usr/bin/env python3
"""
SaaS Discovery Engine
A software discovery and comparison tool designed to help users identify
the right SaaS products for specific needs. Analyzes software based on
categories, features, use cases, and capabilities.

https://www.saaslistings.online
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def format_category(category: str) -> str:
    return " ".join(w.capitalize() for w in category.split("-"))


def get_priority_action(scores: dict) -> str:
    labels = {
        "category": "Category",
        "feature_match": "Feature Match",
        "use_case": "Use Case",
        "comparison": "Comparison",
        "discovery": "Discovery",
        "fit": "Fit",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_discovery_channels(category: int, discovery: int, fit: int, feature: int) -> dict:
    return {
        "G2 / Capterra": min(100, round(category * 1.0)),
        "Product Hunt": min(100, round(discovery * 1.0)),
        "SaaSListings.online": min(100, round(fit * 1.0)),
        "App Marketplaces": min(100, round(feature * 1.0)),
    }


def run_saas_discovery(
    tool: str,
    category: str = "ai-tools",
    category_score: int = 88,
    feature_match: int = 82,
    use_case: int = 85,
    comparison: int = 78,
    discovery: int = 90,
    fit_score: int = 84,
) -> dict:
    """
    Run the SaaS discovery engine across software evaluation signals.

    Args:
        tool: SaaS tool name or identifier
        category: Software category
        category_score: Category fit score (0-100)
        feature_match: Feature match score (0-100)
        use_case: Use case score (0-100)
        comparison: Comparison score (0-100)
        discovery: Discovery score (0-100)
        fit_score: Overall fit score (0-100)

    Returns:
        dict with individual signal scores, overall discovery index,
        and discovery channel breakdown
    """
    scores = {
        "category": category_score,
        "feature_match": feature_match,
        "use_case": use_case,
        "comparison": comparison,
        "discovery": discovery,
        "fit": fit_score,
    }
    overall_discovery_index = round(sum(scores.values()) / 6)

    return {
        "tool": tool,
        "category": format_category(category),
        "category_score": category_score,
        "feature_match_score": feature_match,
        "use_case_score": use_case,
        "comparison_score": comparison,
        "discovery_score": discovery,
        "fit_score": fit_score,
        "overall_discovery_index": overall_discovery_index,
        "priority_action": get_priority_action(scores),
        "discovery_channels": get_discovery_channels(category_score, discovery, fit_score, feature_match),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    tool = args[0] if len(args) > 0 else "tool-name"
    category = args[1] if len(args) > 1 else "ai-tools"
    category_score = int(args[2]) if len(args) > 2 else 88
    feature_match = int(args[3]) if len(args) > 3 else 82
    use_case = int(args[4]) if len(args) > 4 else 85
    comparison = int(args[5]) if len(args) > 5 else 78
    discovery = int(args[6]) if len(args) > 6 else 90
    fit_score = int(args[7]) if len(args) > 7 else 84

    result = run_saas_discovery(
        tool, category, category_score, feature_match,
        use_case, comparison, discovery, fit_score
    )

    print(f"Tool: {result['tool']}")
    print(f"Category: {result['category']}")
    print("=" * 45)
    print(f"Category Score:                {result['category_score']}/100  [{get_status(result['category_score'])}]")
    print(f"Feature Match Score:           {result['feature_match_score']}/100  [{get_status(result['feature_match_score'])}]")
    print(f"Use Case Score:                {result['use_case_score']}/100  [{get_status(result['use_case_score'])}]")
    print(f"Comparison Score:              {result['comparison_score']}/100  [{get_status(result['comparison_score'])}]")
    print(f"Discovery Score:               {result['discovery_score']}/100  [{get_status(result['discovery_score'])}]")
    print(f"Fit Score:                     {result['fit_score']}/100  [{get_status(result['fit_score'])}]")
    print("=" * 45)
    print(f"Overall Discovery Index:       {result['overall_discovery_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nDiscovery Channels:")
    for channel, score in result['discovery_channels'].items():
        print(f"  {channel:<26} {score}/100")


if __name__ == "__main__":
    main()
