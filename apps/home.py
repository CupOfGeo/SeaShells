import dash_bootstrap_components as dbc
# from dash import dcc
from dash import html

# needed only if running this as a single page app
# external_stylesheets = [dbc.themes.LUX]

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead

# needed only if running this as a single page app
# if __name__ == '__main__':
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to George Mazzeo's Gallery", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(
                children="Welcome friends family and possible future friends. I moved to Austin and I'm loving it."
                         " I hope you enjoy my work")
                , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(
                children=[
                    'This website is all python using Plotlys Dash on heroku. I want this to be a showcase of my work '
                    'not a blog. It is a gallery of interactive projects and art I want to share with the world.']
            )
                , className="mb-5")
        ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='Fractals',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Lorenz Attractors", href="/lorenz",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                dbc.Col(dbc.Button("More Attractors", href="/attractors",
                                                                   color="primary"),
                                                        className="mt-3")
                                                ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Github',
                                               className="text-center"),
                                       dbc.Row([dbc.Row(dbc.Button("CupOfGeo",
                                                           href="https://github.com/CupOfGeo",
                                                           color="primary",
                                                           ))

                                                ], justify="center")

                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4"),

            dbc.Col(dbc.Card(children=[html.H3(children='Sea Shells',
                                               className="text-center"),
                                       dbc.Row([dbc.Row(dbc.Button("Sea Shells",
                                                  href="/shell",
                                                  color="primary",
                                                  className="mt-3")),

                                            ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=4, className="mb-4")

        ], className="mb-5", justify="center"),

        dbc.Row([
            dbc.Col(html.H3(
                children="Who am I?")
                , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H5(
                children=["Hello I am George.", html.Br(),
                          """Im a python Developer who loves learning and building. I recently graduated Bucknell 
                          University in 2020 as a computer science engineer with a minor in math and physics. I love 
                          giving people the opportunity to interact with the math and code themselves so they can 
                          have a better intuition about whats actually happening other than just looking and some 
                          words or plots. Currently Im very focused on ML/AI and data science. I find a lot of beauty 
                          in chaos and information theory so I like all kinds of data. I want to become someone who 
                          can really help make the world a better place for all earthlings."""])
                , className="mb-4")
        ]),
        dbc.Row([
            dbc.Col(html.H3('Build')
                    , className="mb-4")
        ]),
        dbc.Row([

            dbc.Col(

                html.H5(
                    # links and write descriptions
                    children=["Project list current:",

                              html.Ul([html.Li("This website and moving my ai projects into it"),

                                       ]),

                              "Projects Shelf:",
                              html.Ul([
                                  html.Li(children=["build something with ", html.A("OpenAI's jukebox",
                                                                                    href='https://openai.com/blog/jukebox/')]),

                                  # https://somerandommusicapp.herokuapp.com/
                                  html.Li(children=[html.A("A comparison of Decision Trees vs Neural Nets", href="https://somerandommusicapp.herokuapp.com/")]),

                                  # https://dashboard.heroku.com/apps/jaredsmaps
                                  html.Li(children=[html.A("Optimal Route Planner", href='https://dashboard.heroku.com/apps/jaredsmaps')]),

                                  html.Li("8 deck card counter"),

                                  html.Li("Python Discords code jam"),

                              ]),
                              ])
                # html.Ul([html.Li()]),
                , className="mb-4")
        ]),
        # dbc.Row([
        #     dbc.Col(html.H3('Learn')
        #             , className="mb-4")
        # ]),
        # dbc.Row([
        #     dbc.Col(
        #
        #         html.H5(
        #             children=["Currently taking:",
        #                       # html.Ul([html.Li(children=)]),
        #                       html.Ul([html.Li(children=[
        #                           html.A("Building Modern Python Applications on AWS on coursera",
        #                                  href='https://www.coursera.org/learn/building-modern-python-applications-on-aws'),
        #                           html.A('Machine Learning Engineering for Production', )]),
        #                                # html.Li(children=[]),
        #                                ]),
        #
        #                       "Up next: ",
        #                       html.Ul([
        #                           html.Li(children=[html.A('TensorFlow: Advanced Techniques Specialization',
        #                                                    href='https://www.coursera.org/specializations/tensorflow-advanced-techniques')]),
        #
        #                       ]),
        #
        #                       "Recently completed:",
        #                       html.Ul([
        #                           html.Li(children=[html.A('Machine Learning by Andrew Ng from Standford',
        #                                                    href='https://www.coursera.org/learn/machine-learning')]),
        #                           html.Li(children=[
        #                               html.A('DeepLearning.AI TensorFlow Developer Professional Certificate',
        #                                      href="https://www.coursera.org/professional-certificates/tensorflow-in-practice"),
        #                               ' and passed Tensorflow certification exam', ]),
        #                           html.Li(children=[
        #                               html.A("MIT's intro to deep learning", href='http://introtodeeplearning.com/')]),
        #                       ]),
        #
        #                       ]
        #         )
        #         , className="mb-4")
        # ]),
        dbc.Row([
            dbc.Col(html.H3('Read')
                    , className="mb-4")
        ]),
        dbc.Row([

            dbc.Col(

                html.H5(
                    # The Annotated Turing by Charles Petzold
                    children=["Currently reading: Architecture Patterns with Python Enabling Test-Driven Development, Domain-Driven Design, and Event-Driven Microservices by Bob Gregory Harry Percival", html.Br(),
                              #
                              "reading list:", html.Br(),
                              "Words That Work: It's Not What You Say, It's What People Hear", html.Br(),
                              # 'Grokking Algorithms by Aditya Bhargava', html.Br(),
                              'The Art of Doing Science and Engineering', html.Br(),
                              "Code by Charles Petzoid", html.Br(),
                              "Life 3.0 by Max Tegmark", html.Br(),
                              'Superintelligence by Nick Bostrom', html.Br(),
                              # "Hitch hikers guide to the Galaxy", html.Br(),
                              # 'Dune by Frank Herbert', html.Br(),
                              # "Genius: The Life and Science of Richard Feynman by James Gleick", html.Br(),
                              "Humankind: A hopeful History", html.Br(),
                              "Winning by Jack Welch ", html.Br(),
                              "Immunity by Philipp Dettmer", html.Br(),
                              "The Book of Why by Judea Pearl", html.Br(),
                              ]
                )
                , className="mb-4")
        ]),

        dbc.Row([
            dbc.Col(html.H5(
                children=["Books I read:", html.Br(),
                          "Microservice APIs by José Peralta", html.Br(),
                          "Helgoland by Carlo Rovelli", html.Br(),
                          "Bootstrapping Microservices with Docker, Kubernetes, and Terraform A project-based guide by Ashley Davis", html.Br(),
                          "Human Hacking by Chris Hadnagy with Seth Schulman", html.Br(),
                          "The Data Detective by Tim Harford", html.Br(),
                          "Writing to Persuade by Trish Hall", html.Br(),
                          "Animal Farm &", html.Br(),
                          "1989 by George Orwell", html.Br(),
                          "Effective Python by Brett Slatkin", html.Br(),
                          "Human Capabilities by Stuart Russell", html.Br(),
                          "Zero to One by Peter Thiel", html.Br(),
                          "Lifespan by David Sinclair", html.Br(),
                          "Do Androids Dream of Electric Sheep by Philip K. Dick", html.Br(),
                          "Ultralearning Scott Young", html.Br(),
                          'Atomic Habit by James Clear', html.Br(),
                          'Genius Makers by Cade Metz', html.Br(),
                          "Lost in Math Sabine Hossenfelder", html.Br(),
                          'Programming the Universe Seth Lloyd', html.Br(),
                          'David and Goliath Malcum', html.Br(),
                          'The Physics of Wall street James Owen Weatherall', html.Br(),
                          'the Signal and the Noise by Nate Silver', html.Br(),
                          'Range by David Epstine', html.Br(),
                          'Naked Statistics by Charles Wheelan', html.Br(),
                          'Everybody Lies by Seth Stephens-Davidowitz', html.Br(),
                          'The Code Book by Simon Singh', html.Br(),
                          'Red Notice by Bill Browder', html.Br(),
                          'Talking to stranger by Gladwell', html.Br(),
                          'Astrophysics for people in a hurry by Tyson', html.Br(),
                          'What do you care what other people think by Feynman', html.Br(),
                          'QED by Feynman', html.Br(),
                          'Influence: Science and Practice by Robert Cialdini', html.Br(),
                          'Chaos by james gleick', html.Br(),
                          'The 7 Habits of highly effective people', html.Br(),
                          'Nine pints by Rose George', html.Br(),
                          'The Grand Design by Steven Hawking', html.Br(),
                          'Outliers', html.Br(),
                          'Sapiens', html.Br(),
                          "Surely You're Joking, Mr. Feynman!", html.Br(),
                          ]
            )
                , className="mb-4")
        ]),

    ])

])
#     app.run_server(host='127.0.0.1', debug=True)
