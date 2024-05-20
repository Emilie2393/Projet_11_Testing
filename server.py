import json
from flask import Flask,render_template,request,redirect,flash,url_for
import datetime

def create_app(config):
    def loadClubs():
        with open('clubs.json') as c:
            listOfClubs = json.load(c)['clubs']
            return listOfClubs


    def loadCompetitions():
        with open('competitions.json') as comps:
            listOfCompetitions = json.load(comps)['competitions']
            return listOfCompetitions


    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.config.from_object(config)
    competitions = loadCompetitions()
    clubs = loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html', clubs=clubs)

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        try: 
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            return render_template('welcome.html',club=club,competitions=competitions)
        except IndexError:
            return "Sorry, that email wasn't found.", 404


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            if datetime.datetime.strptime(foundCompetition['date'][:10], '%Y-%m-%d').date() > datetime.date.today():
                return render_template('booking.html',club=foundClub,competition=foundCompetition)
            else:
                return (f"This competition took place on {str(datetime.datetime.strptime(foundCompetition['date'][:10], '%Y-%m-%d').date())} and is no longer available"), 400
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        if placesRequired <= int(club['points']):
            if placesRequired <= 12:
                competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
                club['points'] = int(club['points'])-placesRequired
                flash('Great-booking complete!')
                return render_template('welcome.html', club=club, competitions=competitions)
            else:
                return "You can't book more than 12 places per competition", 400
        else:
            return (f"You don't have enough points. Points available : {club['points']}"), 400

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app

app=create_app({"TESTING": True})