from setuptools import setup, find_packages

# Function to read requirements from requirements.txt file
def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

# Read the content of README.md for long description
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cloudflare-bypass',
    version='0.1.1',
    description='A tool for bypassing Cloudflare CAPTCHA',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tamnguyenvan/cloudflare-bypass',
    author='Tam Nguyen',
    author_email='tamnvhustcc@gmail.com',
    homepage='https://github.com/tamnguyenvan/cloudflare-bypass',
    packages=find_packages(),
    install_requires=get_requirements(),
    package_data={
        'cloudflare_bypass': ['images/*.png', 'images/*.gif'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='cloudflare captcha bypass',
    project_urls={
        'Documentation': 'https://tamnguyenvan.github.io/cloudflare-bypass',
        'Source': 'https://github.com/tamnguyenvan/cloudflare-bypass',
    },
)