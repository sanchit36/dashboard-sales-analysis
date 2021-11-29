def get_sidebar(st, df, elements):
    components = []
    for element in elements:
        comp = st.sidebar.multiselect(
            element['label'],
            options=df[element['feature_name']].unique(),
            default=df[element['feature_name']].unique(),
        )
        components.append(comp)
        if not len(comp):
            st.sidebar.error(element['error'])
    return components