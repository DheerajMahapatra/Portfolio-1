import streamlit as st
import streamlit_shadcn_ui as ui


# ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")

# import streamlit_shadcn_ui as ui


def show():
    col1, col2 = st.columns(2)
    
    with col1:
        st.image("./assests/search.jpg", width=700)
        
        
    with col2:
        trigger_btn = ui.button(text="Trigger Button", key="trigger_btn")

        ui.alert_dialog(show=trigger_btn, title="Alert Dialog", description="This is an alert dialog", confirm_label="OK", cancel_label="Cancel", key="alert_dialog1")

        def main():
            with ui.card(key="card1"):
                ui.element("span", children=["Email"], className="text-gray-400 text-sm font-medium m-1", key="label1")
                ui.element("input", key="email_input", placeholder="Your email")

                ui.element("span", children=["User Name"], className="text-gray-400 text-sm font-medium m-1", key="label2")
                ui.element("input", key="username_input", placeholder="Create a User Name")
                ui.element("button", text="Submit", key="button", className="m-1")
    main()
    