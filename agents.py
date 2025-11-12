# agents.py
import random

def planner_agent(task: str) -> str:
    """Plans steps for the given task."""
    plan = f"Plan for '{task}':\n1. Understand requirements\n2. Collect information\n3. Build and test solution\n4. Review and improve"
    return plan

def researcher_agent(plan: str) -> str:
    """Simulates research or data gathering based on the plan."""
    findings = [
        "Found best practices on similar projects",
        "Analyzed user needs and market trends",
        "Collected technical documentation and datasets"
    ]
    return "Research results:\n" + "\n".join(findings)

def reviewer_agent(output: str) -> tuple[str, int]:
    """Reviews the combined outputs and gives a quality score."""
    comments = [
        "Excellent structure and clarity.",
        "Good logic, but can add more detail.",
        "Well done! Add one more validation step."
    ]
    score = random.randint(7, 10)
    review = random.choice(comments)
    return review, score
