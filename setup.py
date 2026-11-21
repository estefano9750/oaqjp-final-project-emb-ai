from setuptools import setup, find_packages

setup(
    name="emotion-detection",
    version="1.0.0",
    description="Watson NLP emotion detection application",
    packages=find_packages(),
    py_modules=["emotion_detection"],
    install_requires=["requests"],
)
