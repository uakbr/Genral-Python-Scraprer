from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='web-scraping-framework',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A flexible and extendable web scraping framework for static and dynamic websites.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/web-scraping-framework',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
        'beautifulsoup4',
        'selenium',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'scrape=scraper.__main__:main',
        ],
    },
    include_package_data=True,
    keywords='web scraping, BeautifulSoup, Selenium, AI, GPT-4-turbo-preview',
    license='MIT',
    project_urls={
        'Bug Tracker': 'https://github.com/yourusername/web-scraping-framework/issues',
    },
)
