import streamlit as st
from utils.soundcloud_parser import get_soundcloud_embed_code
from utils.url_generator import generate_shareable_url

def main():
    st.set_page_config(page_title="SoundCloud Embed Generator")
    st.title("SoundCloud Embed Generator")

    # User input fields
    soundcloud_link = st.text_input("Enter SoundCloud Link")
    soundcloud_embed_code = st.text_area("Or, paste SoundCloud Embed Code")

    if st.button("Generate"):
        if soundcloud_embed_code:
            embed_code = soundcloud_embed_code
        else:
            embed_code = get_soundcloud_embed_code(soundcloud_link)

        if embed_code:
            shareable_url = generate_shareable_url()
            st.markdown(f"Share this link: {shareable_url}")
            st.markdown(embed_code, unsafe_allow_html=True)
        else:
            st.error("Invalid SoundCloud link or embed code provided.")

if __name__ == "__main__":
    main()
