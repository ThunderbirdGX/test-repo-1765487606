"""
Feature Module

New feature added on feature branch.
"""

class NewFeature:
    """New feature class"""
    
    def __init__(self, name):
        self.name = name
    
    def execute(self):
        """Execute the feature"""
        return f"Executing feature: {self.name}"

# Example usage
if __name__ == "__main__":
    feature = NewFeature("GitHub API Testing")
    print(feature.execute())
