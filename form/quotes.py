import random


def get_random_quote():
    quotes = [
        [
            "The greatest threat to our planet is the belief that someone else will save it.",
            "Robert Swan",
        ],
        ["We won't have a society if we destroy the environment.", "Margaret Mead"],
        ["The Earth does not belong to us: we belong to the Earth.", "Marlee Matlin"],
        [
            "What we are doing to the forests of the world is but a mirror reflection of what we are doing to ourselves and to one another.",
            "Mahatma Gandhi",
        ],
        [
            "The Earth does not yield its best fruits unless the heart is opened to love and thanksgiving.",
            "Pope Francis",
        ],
        ["The future will either be green or not at all.", "Bob Brown"],
        [
            "We do not inherit the earth from our ancestors, we borrow it from our children.",
            "Native American Proverb",
        ],
        [
            "The environment is where we all meet; where we all have a mutual interest; it is the one thing all of us share.",
            "Lady Bird Johnson",
        ],
        [
            "Earth provides enough to satisfy every man's needs, but not every man's greed.",
            "Mahatma Gandhi",
        ],
        [
            "The more clearly we can focus our attention on the wonders and realities of the universe about us, the less taste we shall have for destruction.",
            "Rachel Carson",
        ],
        [
            "What we are doing to the forests of the world is but a mirror reflection of what we are doing to ourselves and to one another.",
            "Mahatma Gandhi",
        ],
        ["We won't have a society if we destroy the environment.", "Margaret Mead"],
        ["The Earth does not belong to us: we belong to the Earth.", "Marlee Matlin"],
        ["He that plants trees loves others beside himself.", "Thomas Fuller"],
        [
            "A nation that destroys its soils destroys itself. Forests are the lungs of our land, purifying the air and giving fresh strength to our people.",
            "Franklin D. Roosevelt",
        ],
        ["Nature is not a place to visit. It is home.", "Gary Snyder"],
        ["We won't have a society if we destroy the environment.", "Margaret Mead"],
        [
            "The Earth does not yield its best fruits unless the heart is opened to love and thanksgiving.",
            "Pope Francis",
        ],
        ["What we save, saves us.", "Anonymous"],
        ["We won't have a society if we destroy the environment.", "Margaret Mead"],
        [
            "The environment is where we all meet; where we all have a mutual interest; it is the one thing all of us share.",
            "Lady Bird Johnson",
        ],
        [
            "Earth provides enough to satisfy every man's needs, but not every man's greed.",
            "Mahatma Gandhi",
        ],
        [
            "The future belongs to those who understand that doing more with less is compassionate, prosperous, and enduring, and thus more intelligent, even competitive.",
            "Paul Hawken",
        ],
        [
            "The best time to plant a tree was 20 years ago. The second-best time is now.",
            "Chinese Proverb",
        ],
    ]

    random_quote = random.choice(quotes)
    return random_quote
