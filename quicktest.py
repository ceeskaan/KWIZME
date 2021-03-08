#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pipelines import pipeline

if __name__ == '__main__':
    model = pipeline("question-generation")

    text = "42 is the answer to life, universe and everything."
    print(text)
    questions = model(text)
    print(questions)