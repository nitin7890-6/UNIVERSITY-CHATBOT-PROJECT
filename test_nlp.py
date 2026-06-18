from app.nlp import recognize_intent


def test_recognize_admissions():
    intent, conf = recognize_intent("How do I apply for admission?")
    assert intent == "admissions"
    assert conf > 0


def test_recognize_exams():
    intent, conf = recognize_intent("When are the final exams?")
    assert intent == "examinations"
    assert conf > 0


def test_fallback():
    intent, conf = recognize_intent("")
    assert intent == "fallback"
    assert conf == 0.0
