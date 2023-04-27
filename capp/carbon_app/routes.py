from flask import render_template, Blueprint, request, redirect, url_for, flash
from capp.models import Transport
from capp import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from capp.carbon_app.forms import BusForm, CarForm, PlaneForm, TrainForm, ElkickScooterForm, ElBicycleForm

carbon_app=Blueprint('carbon_app',__name__)

#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.10231,'BioDiesel':0.08,'Electric':0.0133},
    'Car':{'Gasoline':0.18592,'Diesel':0.16453,'Hybrid':0.10,'No Fossil Fuel':0.0133},
    'Plane':{'Gasoline':0.24298},
    'Train':{'No Fossil Fuel':0.0133},
    'ElkickScooter':{'No Fossil Fuel':0.0133},
    'ElBicyle':{'No Fossil Fuel':0.0133}}


#Carbon app, main page
@carbon_app.route('/carbon_app')
@login_required
def carbon_app_home():
    return render_template('carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@carbon_app.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@carbon_app.route('/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@carbon_app.route('/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry Train
@carbon_app.route('/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_train.html', title='new entry Train', form=form)     

#New entry ElkickScooter
@carbon_app.route('/carbon_app/new_entry_ElkickScooter', methods=['GET','POST'])
@login_required
def new_entry_ElkickScooter():
    form = ElkickScooterForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'ElkickScooter'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_ElkickScooter.html', title='new entry motorbike', form=form) 

#New entry ElBicyleForm
@carbon_app.route('/carbon_app/new_entry_ElBicyle', methods=['GET','POST'])
@login_required
def new_entry_ElBicycle():
    form = ElBicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'ElBicyle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = Transport(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('carbon_app/new_entry_Elbicycle.html', title='new entry Elbicycle', form=form)


#Your data
@carbon_app.route('/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = Transport.query.filter_by(author=current_user). \
        filter(Transport.date> (datetime.now() - timedelta(days=5))).\
        order_by(Transport.date.desc()).order_by(Transport.transport.asc()).all()
    return render_template('carbon_app/your_data.html', title='your_data', entries=entries)

#Delete emission
@carbon_app.route('/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = Transport.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('carbon_app.your_data'))
    
  
