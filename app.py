
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="DevOps portfolio and resume of Ayush Asthana">
        <title>Ayush Asthana | DevOps Portfolio</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            html {
                scroll-behavior: smooth;
            }

            body {
                font-family: Arial, Helvetica, sans-serif;
                background: #0b1120;
                color: #e2e8f0;
                line-height: 1.7;
            }

            a {
                color: #38bdf8;
                text-decoration: none;
            }

            a:hover {
                color: #7dd3fc;
            }

            .container {
                width: 90%;
                max-width: 1050px;
                margin: auto;
            }

            header {
                padding: 20px 0;
                border-bottom: 1px solid #243047;
            }

            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 20px;
                flex-wrap: wrap;
            }

            .logo {
                font-size: 21px;
                font-weight: bold;
                color: #f8fafc;
            }

            nav a {
                margin-left: 18px;
                color: #cbd5e1;
                font-size: 14px;
            }

            .hero {
                padding: 90px 0 70px;
            }

            .tag {
                display: inline-block;
                color: #7dd3fc;
                border: 1px solid #164e63;
                background: #102638;
                padding: 6px 13px;
                border-radius: 20px;
                font-size: 13px;
                margin-bottom: 22px;
            }

            h1 {
                font-size: clamp(38px, 6vw, 64px);
                line-height: 1.15;
                color: #f8fafc;
                margin-bottom: 20px;
            }

            h1 span {
                color: #38bdf8;
            }

            .hero p {
                max-width: 720px;
                color: #aab8cc;
                font-size: 17px;
                margin-bottom: 28px;
            }

            .button {
                display: inline-block;
                background: #0284c7;
                color: white;
                padding: 12px 20px;
                border-radius: 7px;
                margin: 5px 8px 5px 0;
                font-weight: bold;
            }

            .button:hover {
                background: #0369a1;
                color: white;
            }

            .button.secondary {
                background: transparent;
                border: 1px solid #475569;
            }

            section {
                padding: 55px 0;
                border-top: 1px solid #1e293b;
            }

            h2 {
                font-size: 29px;
                color: #f8fafc;
                margin-bottom: 24px;
            }

            .section-intro {
                color: #aab8cc;
                max-width: 760px;
                margin-bottom: 24px;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
                gap: 18px;
            }

            .card {
                background: #111c30;
                border: 1px solid #26344b;
                border-radius: 12px;
                padding: 23px;
            }

            .card h3 {
                color: #7dd3fc;
                margin-bottom: 10px;
                font-size: 18px;
            }

            .card p, .card li {
                color: #b6c3d5;
                font-size: 14px;
            }

            ul {
                padding-left: 20px;
            }

            li {
                margin-bottom: 8px;
            }

            .project {
                margin-bottom: 18px;
            }

            .project h3 {
                color: #f8fafc;
                font-size: 20px;
                margin-bottom: 8px;
            }

            .tech {
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 14px;
            }

            .tech span {
                background: #1e293b;
                border: 1px solid #334155;
                color: #bae6fd;
                padding: 4px 10px;
                border-radius: 5px;
                font-size: 12px;
            }

            .contact {
                background: #111c30;
                border: 1px solid #26344b;
                border-radius: 12px;
                padding: 28px;
            }

            footer {
                text-align: center;
                padding: 28px 0;
                color: #8190a5;
                font-size: 13px;
            }

            @media (max-width: 600px) {
                nav {
                    align-items: flex-start;
                }

                nav a {
                    margin: 0 12px 0 0;
                    display: inline-block;
                }

                .hero {
                    padding-top: 60px;
                }
            }
        </style>
    </head>

    <body>
        <header>
            <div class="container">
                <nav>
                    <div class="logo">Ayush Asthana.</div>
                    <div>
                        <a href="#about">About</a>
                        <a href="#skills">Skills</a>
                        <a href="#projects">Projects</a>
                        <a href="#contact">Contact</a>
                    </div>
                </nav>
            </div>
        </header>

        <main>
            <div class="container">
                <section class="hero" style="border-top: none;">
                    <span class="tag">DEVOPS PORTFOLIO</span>
                    <h1>Hi, I'm Ayush Asthana.<br>
                    I build and deploy <span>applications.</span></h1>

                    <p>
                        Computer Science graduate focused on DevOps and cloud
                        technologies. I have built a containerized Flask
                        application and implemented an automated CI/CD pipeline
                        using GitHub Actions, Docker Hub and Microsoft Azure.
                    </p>

                    <a class="button" href="#projects">Explore My Project</a>
                    <a class="button secondary" href="#contact">Contact Me</a>
                </section>

                <section id="about">
                    <h2>About Me</h2>
                    <p class="section-intro">
                        I am interested in building reliable application
                        delivery workflows, learning cloud infrastructure and
                        automating repetitive deployment tasks. My project
                        experience includes containerization, automated
                        testing, image publishing and cloud deployment.
                    </p>

                    <div class="grid">
                        <div class="card">
                            <h3>Cloud & Deployment</h3>
                            <p>
                                Deployed a Flask application to Azure Container
                                Apps and configured a custom domain with HTTPS.
                            </p>
                        </div>

                        <div class="card">
                            <h3>Automation</h3>
                            <p>
                                Created a GitHub Actions workflow to run tests,
                                build a Docker image and automate deployment.
                            </p>
                        </div>

                        <div class="card">
                            <h3>Problem Solving</h3>
                            <p>
                                Practiced Linux commands, application
                                troubleshooting and verification of deployment
                                results.
                            </p>
                        </div>
                    </div>
                </section>

                <section id="skills">
                    <h2>Technical Skills</h2>
                    <p class="section-intro">
                        Technologies used in my project and technical practice.
                    </p>

                    <div class="grid">
                        <div class="card">
                            <h3>DevOps & CI/CD</h3>
                            <ul>
                                <li>Git and GitHub</li>
                                <li>GitHub Actions</li>
                                <li>CI/CD pipeline automation</li>
                            </ul>
                        </div>

                        <div class="card">
                            <h3>Containers & Cloud</h3>
                            <ul>
                                <li>Docker</li>
                                <li>Docker Hub</li>
                                <li>Microsoft Azure Container Apps</li>
                            </ul>
                        </div>

                        <div class="card">
                            <h3>Development & Testing</h3>
                            <ul>
                                <li>Python and Flask</li>
                                <li>Unit testing with unittest</li>
                                <li>HTTP endpoint verification</li>
                            </ul>
                        </div>

                        <div class="card">
                            <h3>Linux & Other Skills</h3>
                            <ul>
                                <li>Ubuntu on WSL</li>
                                <li>Linux commands and permissions</li>
                                <li>Basic SQL and Power BI</li>
                            </ul>
                        </div>
                    </div>
                </section>

                <section id="projects">
                    <h2>Featured Project</h2>

                    <div class="card project">
                        <h3>End-to-End DevOps CI/CD Pipeline</h3>
                        <p>
                            Developed and deployed a Python Flask web
                            application using Docker and Microsoft Azure.
                            Automated the delivery workflow with GitHub
                            Actions to run unit tests, build and validate the
                            container image, publish versioned images to Docker
                            Hub, and deploy updates to Azure Container Apps.
                        </p>

                        <ul style="margin-top: 14px;">
                            <li>Created a Dockerfile to package the Flask application.</li>
                            <li>Added automated unit tests to validate application behavior.</li>
                            <li>Configured GitHub Actions for continuous integration and deployment.</li>
                            <li>Published Docker images with commit-based tags and a latest tag.</li>
                            <li>Configured Azure deployment using GitHub Actions and OpenID Connect.</li>
                            <li>Connected a custom domain and configured an Azure-managed HTTPS certificate.</li>
                        </ul>

                        <div class="tech">
                            <span>Python</span>
                            <span>Flask</span>
                            <span>Linux</span>
                            <span>Docker</span>
                            <span>GitHub Actions</span>
                            <span>Docker Hub</span>
                            <span>Microsoft Azure</span>
                            <span>CI/CD</span>
                        </div>

                        <p style="margin-top: 18px;">
                            <a href="https://github.com/Ayux1/devops-project"
                               target="_blank" rel="noopener noreferrer">
                                View Source Code on GitHub →
                            </a>
                        </p>
                    </div>
                </section>

                <section id="education">
                    <h2>Education</h2>
                    <div class="card">
                        <h3>Computer Science / Information Technology</h3>
                        <p>
                            MCA | Galgotias University (7 cgpa) | BCA | VBSPU (8 cgpa)
                        </p>
                    </div>
                </section>

                <section id="contact">
                    <h2>Let's Connect</h2>
                    <div class="contact">
                        <p class="section-intro">
                            I'm interested in entry-level DevOps, cloud
                            engineering and system engineering opportunities.
                            Feel free to connect with me.
                        </p>

                        <p>
                            GitHub:
                            <a href="https://github.com/Ayux1"
                               target="_blank" rel="noopener noreferrer">
                                github.com/Ayux1
                            </a>
                        </p>

                        <p style="margin-top: 10px;">
                            LinkedIn: https://www.linkedin.com/in/ayush-asthana-11168b210/
                        </p>

                        <p style="margin-top: 10px;">
                            Email: in.ayush17@gmail.com
                        </p>
                    </div>
                </section>
            </div>
        </main>

        <footer>
            <div class="container">
                © 2026 Ayush Asthana | DevOps Portfolio
            </div>
        </footer>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
