from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="saas-discovery-engine",
    version="1.0.0",
    author="SaaSListings.online",
    author_email="info@saaslistings.online",
    description="SaaS Discovery Engine is a software discovery and comparison tool designed to help users identify the right SaaS products for specific needs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.saaslistings.online",
    project_urls={
        "Homepage": "https://www.saaslistings.online",
        "GitHub": "https://github.com/saaslistings/saas-discovery-engine",
        "Documentation": "https://saas-discovery-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/saas-discovery-engine",
    },
    py_modules=["saas_discovery"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
        "Topic :: Software Development",
    ],
    keywords=[
        "saas-discovery-engine",
        "software-comparison",
        "saas-categories",
        "feature-analysis",
        "use-case-scoring",
        "ai-tools-discovery",
        "business-software",
        "saaslistings",
    ],
    entry_points={
        "console_scripts": [
            "saas-discover=saas_discovery:main",
        ],
    },
)
