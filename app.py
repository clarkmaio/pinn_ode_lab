import panel as pn
import numpy as np
import pandas as pd
import holoviews as hv

# Crea dati casuali
np.random.seed(0)
data = pd.DataFrame(np.random.randn(100, 2), columns=['X', 'Y'])

# Crea la funzione per generare il grafico
def create_line_plot():
    return hv.Curve(data, 'X', 'Y').opts(width=600, height=400)

# Crea la funzione per aggiornare il grafico in base all'input dell'utente
def update_plot(event):
    new_data = pd.DataFrame(np.random.randn(100, 2), columns=['X', 'Y'])
    plot_object.data = new_data

# Creazione dei componenti interattivi
line_plot = create_line_plot()
update_button = pn.widgets.Button(name='Aggiorna Dati', button_type='primary')
update_button.on_click(update_plot)

# Assembla la dashboard
dashboard = pn.Column(
    "# Semplice Dashboard con Panel",
    line_plot,
    update_button
)

# Visualizza la dashboard
dashboard.servable()
