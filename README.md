
######################################Operation "Mirrortgv2"##################################################

## Guiding Principles (The Constitution)

*   **Absolute Fidelity:** The primary directive is to replicate messages with 100% accuracy. No data is added, removed, or altered.
*   **Discipline Over Creativity:** The code follows a strict, minimalist protocol. There are no unnecessary features.
*   **Stealth Operation:** Messages are re-created, not forwarded. This prevents any link back to the original source.
*   **Reliability:** Engineered for stable, continuous 24/7 operation in a cloud environment.

## Deployment: Establishing the Operations Base (Render.com)

This protocol is designed for a 24/7 cloud deployment. Local execution is for testing purposes only. The recommended base of operations is Render.

**Phase 1: Get Your Credentials**

1.  Go to [my.telegram.org](https://my.telegram.org) and log in.
2.  Navigate to "API development tools" and obtain your `API_ID` and `API_HASH`.
3.  Obtain the IDs for your source and target channels.

**Phase 2: Deploy to Render**

1.  **Fork** this repository to your own GitHub account.
2.  Go to the [Render Dashboard](https://dashboard.render.com/) and create a **New Web Service**.
3.  Connect the GitHub repository you just forked.
4.  Configure the service with the following settings:
    *   **Runtime:** `Python 3`
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `python copybot.py`
    *   **Instance Type:** `Free`

**Phase 3: Securely Input Your Orders (Environment Variables)**

Do not upload your secret credentials to GitHub. Input them directly into the Render base.

1.  In your Render service dashboard, go to the **Environment** tab.
2.  Under **Environment Variables**, add the following keys and their corresponding values:

| Key               | Description                                          | Example Value       |
| ----------------- | ---------------------------------------------------- | ------------------- |
| `API_ID`          | Your Telegram application ID.                        | `1234567`           |
| `API_HASH`        | Your Telegram application hash.                      | `abcdef123456...`   |
| `SESSION_NAME`    | A unique name for the session file.                  | `ghost-session`     |
| `KAYNAK_KANAL_ID` | The ID of the source channel. (Must start with -100) | `-100123456789`     |
| `HEDEF_KANAL_ID`  | The ID of the target channel. (Must start with -100) | `-100987654321`     |

3.  Click **Save Changes**. The service will automatically deploy with these credentials.

## Local Testing (Optional)

1.  Clone the repository: `git clone [your-repo-url]`
2.  Install requirements: `pip install -r requirements.txt`
3.  Create an `ayarlar.txt` file in the same directory with the following format:
    ```
    API_ID = 1234567
    API_HASH = abcdef123456...
    SESSION_NAME = ghost-session
    KAYNAK_KANAL_ID = -100123456789
    HEDEF_KANAL_ID = -100987654321
    ```
4.  Start the protocol: `python copybot.py`

> **WARNING:** Never commit the `ayarlar.txt` file or your session file to a public repository.

---

## Legal Disclaimer & Responsibility

This software is provided for educational and experimental purposes only.

The end-user is **solely responsible** for their actions and must comply with all applicable local, state, national, and international laws, as well as Telegram's Terms of Service. Automating user accounts may violate these terms.

The author of this software does **not** endorse, support, or condone its use for any illegal activities, including but not limited to harassment, copyright infringement, or the dissemination of prohibited content.

Any actions and consequences resulting from the use of this software are the **sole responsibility of the user**. The author accepts no liability for any misuse, damage, account restriction, or legal repercussions caused by this protocol. Use at your own risk.
