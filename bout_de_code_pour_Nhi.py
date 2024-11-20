    # Filtres pour une date unique
    selected_date = st.sidebar.date_input(
        "Sélectionnez une date",
        value=data['Last Updated'].min().date(),
        min_value=data['Last Updated'].min().date(),
        max_value=data['Last Updated'].max().date()
    )

    filtered_data = data[
        (data['Pollutant'] == selected_pollutant) &
        (data['Country Label'] == selected_country) &
        (data['Last Updated'].dt.date == selected_date)
    ]
