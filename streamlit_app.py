import streamlit as st
import re
import uuid

def get_soundcloud_embed_code(soundcloud_link):
    """
    Extract the necessary information from the SoundCloud link and generate the embed code.
    """
    try:
        # Extract the track or playlist ID from the link
        if "tracks" in soundcloud_link:
            track_id = re.search(r"tracks\/(\d+)", soundcloud_link).group(1)
            embed_code = f'<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/{track_id}&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>'
        elif "playlists" in soundcloud_link:
            playlist_id = re.search(r"playlists\/(\d+)", soundcloud_link).group(1)
            embed_code = f'<iframe width="100%" height="450" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/{playlist_id}&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>'
        else:
            return None
        return embed_code
    except (AttributeError, IndexError):
        return None

def generate_shareable_url():
    """
    Generate a unique, shareable URL for the generated SoundCloud embed page.
    """
    unique_id = str(uuid.uuid4())[:8]
    shareable_url = st.beta_set_page_config(page_url=f"/soundcloud-embed/{unique_id}")
    return shareable_url

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
