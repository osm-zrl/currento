from flask import Flask, render_template

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from io import BytesIO
import base64
from dbconfig import daily_average
from dbconfig import last_day_data
from api_connector import get_data


app = Flask(__name__)

def generate_chart():
    result = list(reversed(daily_average()))
    
    dates = [entry['_id'] for entry in result]
    mad_rates = [entry['MAD'] for entry in result]
    usd_rates = [entry['USD'] for entry in result]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, mad_rates, marker='o', linestyle='-', label='MAD Rates')
    plt.plot(dates, usd_rates, marker='o', linestyle='-', label='USD Rates')
    plt.title('MAD and USD For Last 7 days')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    img_tag = f'<img class="img-fluid img-thumbnail rounded" src="data:image/png;base64,{img_base64}">'
    plt.close()

    return img_tag

def mad_generate_chart():
    result = list(reversed(daily_average()))
    dates = [entry['_id'] for entry in result]
    mad_rates = [entry['MAD'] for entry in result]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, mad_rates, marker='o', linestyle='-', label='MAD Rates')
    plt.title('MAD For Last 7 days')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    img_tag = f'<img class="img-fluid img-thumbnail rounded" src="data:image/png;base64,{img_base64}">'
    plt.close()

    return img_tag

def usd_generate_chart():
    result = list(reversed(daily_average()))
    dates = [entry['_id'] for entry in result]
    usd_rates = [entry['USD'] for entry in result]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, usd_rates, marker='o', linestyle='-', label='USD Rates')
    plt.title('USD For Last 7 days')
    plt.xlabel('Date')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    img_tag = f'<img class="img-fluid img-thumbnail rounded" src="data:image/png;base64,{img_base64}">'
    plt.close()

    return img_tag

def last_day_generate_chart():
    result = list(last_day_data())
    dates = [entry['timestamp'] for entry in result]
    mad_rates = [entry['rates']['MAD'] for entry in result]
    usd_rates = [entry['rates']['USD'] for entry in result]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, mad_rates, marker='o', linestyle='-', label='MAD Rates')
    plt.plot(dates, usd_rates, marker='o', linestyle='-', label='USD Rates')
    plt.title(f'MAD and USD For last 24 hours')
    plt.xlabel('Time')
    plt.ylabel('Rate')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()
    img_tag = f'<img class="img-fluid img-thumbnail rounded" src="data:image/png;base64,{img_base64}">'
    plt.close()

    return img_tag

@app.route('/')
def index():
    todayData = get_data()
    last_chart = last_day_generate_chart()
    mad_chart = mad_generate_chart()
    usd_chart = usd_generate_chart()
    chart = generate_chart()
    
    return render_template('index.html', mad=todayData['rates']['MAD'],usd=todayData['rates']['USD'],last_day = last_chart , daily_chart=chart,daily_chart_mad=mad_chart,daily_chart_usd=usd_chart)

@app.route('/about')
def about():
    return render_template('about.html', name='User')

if __name__ == '__main__':
    app.run(debug=False)