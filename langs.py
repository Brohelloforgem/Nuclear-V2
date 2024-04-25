import config_selfbot

#######################
#  selfbot            #
#    translation >.<  #
#######################

token_error = {
    "fr": "Token incorrect. Merci d'entrer un token valide dans config_selfbot.py",
    "en": "Improper token. Please configure a valid token in config_selfbot.py"
}

aihottp_error = {
    "fr": "Ancienne version d'aiohttp (cette erreur de vient pas de Nuclear ^^). Cette erreur vient de discord.py==1.7.3, Tentaive de fix (le selfbot va redémarrer!)...\nAppuyez sur Entrer.",
    "en": "Old aiohttp error (not Nuclear's fault ^^). This comes from discord.py==1.7.3, trying to fix it (it will restart!)...\nPress Enter."
}

aihottp_success = {
    "fr": "Redémarrage en cours...",
    "en": "Restarting..."
}

weird_error = {
    "fr": "Maybe a config error. Make sure all information in config_selfbot.py are correct.\nError:",
    "en": "Peut-être une erreur de configuration. Assurez-vous que toutes les informations dans config_selfbot.py sont correctes.\nErreur:"
}

cog_success = {
    "fr": "Catégorie chargé avec succès !",
    "en": "Successfully loaded category!"
}

cog_fail = {
    "fr": "Erreur lors du chargement de cette catégorie: ",
    "en": "Error while trying to load catergory: "
}

enable = {
    "fr": "activé !",
    "en": "enabled!"
}

disable = {
    "fr": "désactivé !",
    "en": "disabled!"
}

empty = {
    "fr": "Aucune",
    "en": "Empty"
}

author = {
    "fr": "Auteur",
    "en": "Author"
}

####################
#  launch          #
# translation !!!  #
####################

start_text = {
    "fr": "Démarrage du selfbot en cours...",
    "en": "Starting the selfbot..."
}

ready_text = {
    "fr": "Connecté en tant que",
    "en": "Connected as"
}

ready_text_two = {
    "fr": "démarré en",
    "en": "started in"
}

ready_text_three = {
    "fr": "secondes.",
    "en": "seconds."
}

error_check_version_one = {
    "fr": "Une nouvelle version",
    "en": "A new version"
}

error_check_version_two = {
    "fr": "est disponible:",
    "en": "is out at:"
}

error_check_version_three = {
    "fr": "Vous utilisez actuellement la version ",
    "en": "You are currently using "
}

####################
#  help            #
# translation !!!  #
####################



help_voice = {
    "fr": "Vocal",
    "en": "Voice"
}


help_general_hype = {
    "fr": "Défini votre badge HypeSquad",
    "en": "Set your HypeSquad badge"
}

help_general_ping = {
    "fr": "Affiche la latence du selfbot",
    "en": "Display the selfbot's ping"
}

help_general_sniper = {
    "fr": "Active / désactive le NitroSniper",
    "en": "Enable / disable NitroSniper"
}

error_no_message_snipe = {
    "fr": "❌ Aucun message supprimé récemment dans ce salon !",
    "en": "❌ No message deleted recently in this channel!"
}

help_config_restart = {
    "fr": "Redémarre le selfbot (peut régler un bug)",
    "en": "Restart the selfbot. (it can fix a bug)"
}

help_config_stop = {
    "fr": "Stop le selfbot",
    "en": "Stop the selfbot"
}

help_general_bio = {
    "fr": "Change la biographie du compte",
    "en": "Change account's bio"
}

help_general_snipe = {
    "fr": "Snipe le dernier message supprimé.",
    "en": "Snipe the last deleted message."
}

help_general_clear = {
    "fr": "Supprime le nombre de messages fourni.",
    "en": "Clear given number of messages."
}

help_voice_vc = {
    "fr": "Rejoins le salon vocal",
    "en": "Join the voice channel"
}

help_voice_cam = {
    "fr": "Rejoins le salon vocal avec une fausse caméra",
    "en": "Join the voice channel with a fake camera"
}

help_voice_leave = {
    "fr": "Quitte le salon vocal",
    "en": "Leave the voice channnel"
}

help_fun_cat = {
    "fr": "Chat mignon 🐈",
    "en": "Cute cat 🐈"
}

help_fun_good = {
    "fr": "Vous transforme en une Bonne Personne ! (*censure les insultes*)",
    "en": "Transform you into a Good Person ! (*no insults*)"
}

help_fun_call = {
    "fr": "Spam d'appel (seulement en MP!)",
    "en": "Join and Leave the voice (only in dm!)"
}

help_fun_gift = {
    "fr": "Envoie un faux lien Nitro",
    "en": "Send a fake Nitro"
}

help_raid_dmall = {
    "fr": "Envoi un message privé à votre liste d'amis",
    "en": "Send a private message to your friend list."
}

help_raid_banall = {
    "fr": "Bannis tout les membres du serveur",
    "en": "Ban all members"
}

help_raid_kick = {
    "fr": "Kick tout les membres du serveur",
    "en": "Kick all members."
}

help_tools_close_dm = {
    "fr": "Ferme tout vos MP",
    "en": "Close all your DMs"
}

help_tools_close_dm_bots = {
    "fr": "Ferme tout vos MP avec des bots",
    "en": "Close all your DMs with bots"
}


####################
#  commands        #
# translation !!!  #
####################

restart_command = {
    "fr": "✅ Selfbot redémarré avec succès (patientez quelques secondes...) !",
    "en": "✅ Succesfully restarted the selfbot (wait a couple of seconds...)!"
}

stop_command = {
    "fr": "⭕ Le selfbot a bien été stoppé.",
    "en": "⭕ Succesfully stopped the selfbot."
}

leave_voice = {
    "fr": "Déconnection du salon",
    "en": "Disconnected from"
}

leave_voice_error = {
    "fr": "Error while leaving the voice channel",
    "en": "Erreur lors de la déconnexion au salon vocal"
}

leave_voice_error_not_found = {
    "fr": "❌ Vous devez être connecté à un salon vocal pour utiliser cette commande !",
    "en": "❌ You must be connected to a voice channel to use this command!"
}

voice_channel_error = {
    "fr": "❌ Veuillez indiquer un ID de salon vocal valide !",
    "en": "❌ Please enter a valid voice channel ID!"
}

voice_not_dm = {
    "fr": "❌ Cette commande n'est pas disponible en MP!",
    "en": "❌ You can't use this command in DMs!"
}

voice_channel_error_not_found = {
    "fr": "❌ Le salon vocal avec cet ID n'existe pas.",
    "en": "❌ Unable to find the voice channel!"
}

hype_command = {
    "fr": "modifié en",
    "en": "changed to"
}

hype_fail = {
    "fr": "❌ HypeSquad renseignée incorrect. (brilliance, balance, bravery).",
    "en": "❌ Given HypeSquad house is incorrect. (brilliance, balance, bravery)."
}

bio_command = {
    "fr": "changée en",
    "en": "changed to"
}

spam_cooldown = {
    "fr": f"❌ Un spam est déjà en cours ! Pour l'arrêter, faites `{config_selfbot.prefix}restart`.",
    "en": f"❌ A spam is already active! To spam the current spam, do `{config_selfbot.prefix}restart`."
}

spam_invalid = {
    "fr": "❌ Veuillez indiquer un nombre valide !",
    "en": "❌ You must enter a valid number!"
}

spam_too_much = {
    "fr": "❌ Veulliez indiquer une valeur en dessous de 100 !",
    "en": "❌ Please enter a value below 100!"
}

only_dm_fun = {
    "fr": "❌ Cette commande n'est disponible qu'en MP!",
    "en": "❌ You must use this command in DM!"
}

voice_join = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to"
}

voice_join_error = {
    "fr": "Erreur lors de la connexion au salon vocal",
    "en": "Error while trying to connect to the voice channel"
}

voice_join_cam = {
    "fr": "Connecté au salon vocal",
    "en": "Connected to"
}

voice_join_cam_two = {
    "fr": "avec la caméra activée",
    "en": "with camera"
}

nitro_sniper_claimed = {
    "fr": "a déjà été réclamé par quelqu'un d'autre !",
    "en": "was already redeemed by someone else!"
}

nitro_sniper_valid = {
    "fr": "a bien été réclamé sur le compte !",
    "en": "has been claimed on the account!"
}

nitro_sniper_invalid_code = {
    "fr": "est invalide !",
    "en": "is invalid!"
}

raid_in_process = {
    "fr": "☣️ Raid en cours...",
    "en": "☣️ Raid in progress..."
}

raid_error_permisssion = {
    "fr": "‼️ Permission manquantes !",
    "en": "‼️ Missing permissions!"
}

raid_kick_all_success = {
    "fr": "✅ Tout les membres ont été kick du serveur avec succès.",
    "en": "✅ Succesfully kicked all members."
}

raid_ban_all_success = {
    "fr": "✅ Tout les membres ont été bannis du serveur avec succès.",
    "en": "✅ Succesfully banned all members."
}

raid_dm_all = {
    "fr": "☣️ Envoi du message privée à toute la liste d'amis...",
    "en": "☣️ Sending the message to all friends..."
}

raid_dm_all_fail = {
    "fr": "❌ Vous devez renseigner un message !",
    "en": "❌ You must enter a message!"
}

raid_dm_all_captcha = {
    "fr": "❌ Amis trop nombreux. Captcha requis !",
    "en": "❌ Too many friends. Captcha required!"
}

raid_dm_all_success = {
    "fr": "✅ Message envoyé avec succès à la liste d'amis !",
    "en": "✅ Succesfully sent message to all friends!"
}

tool_close_dms = {
    "fr": "🔧 Fermeture de tout vos MP...",
    "en": "🔧 Closing all your DMs..."
}

tool_close_dms_success = {
    "fr": "✅ Tout vos MP ont bien été fermés !",
    "en": "✅ All of your DMs has been closed!"
}

tool_close_dms_bots = {
    "fr": "🔧 Fermeture de tout vos MP avec des bots...",
    "en": "🔧 Closing all your DMs with bots..."
}

tool_close_dms_bots_success = {
    "fr": "✅ Tout vos MP avec des bots ont bien été fermés !",
    "en": "✅ All of your DMs with bots has been closed!"
}

####################
#  rpc             #
# translation !!!  #
####################




rpc_status_translate = {
    "fr": "Défini le statut du RPC",
    "en": "Set RPC's status"
}

rpc_name_translate = {
    "fr": "Défini le nom du RPC",
    "en": "Set RPC's name"
}

rpc_details_translate = {
    "fr": "Défini les details du RPC",
    "en": "Set RPC's details"
}

rpc_state_translate = {
    "fr": "Défini le \"state\" du RPC",
    "en": "Set RPC's state"
}

rpc_url_translate = {
    "fr": "Défini l'url de steaming du RPC ``(https://twitch.tv/nom)``",
    "en": "Set RPC's streaming URL ``(https://twitch.tv/name)``"
}

rpc_type_translate = {
    "fr": "Défini le type de votre RPC (game / watch / listen / stream)",
    "en": "Set RPC's type (game / watch / listen / stream)"
}

rpc_id_translate = {
    "fr": "Défini l'ID de l'application pour le RPC",
    "en": "Set RPC's Application ID"
}

rpc_image_translate = {
    "fr": "Défini l'image du RPC",
    "en": "Set RPC's image"
}

rpc_button_text_one_translate = {
    "fr": "Défini le texte du premier bouton du RPC",
    "en": "Set RPC's first button text"
}

rpc_button_link_one_translate = {
    "fr": "Défini le lien du premier bouton du RPC",
    "en": "Set RPC's first button link"
}

rpc_button_text_two_translate = {
    "fr": "Défini le texte du second bouton du RPC",
    "en": "Set RPC's second button text"
}

rpc_button_link_two_translate = {
    "fr": "Défini le lien du second bouton du RPC",
    "en": "Set RPC's second button link"
}




####################
# template         #
# translation !!!  #
####################

template_help_reset = {
    "fr": "Réinitialise votre RPC.",
    "en": "Reset your RPC."
}

template_help_default = {
    "fr": "Modifie votre RPC par celui présent dans (`config_selfbot.py`).",
    "en": "Edit your RPC to the default one (in `config_selfbot.py`)."
}

template_help_cod = {
    "fr": "Utilise la template \"Call Of Duty\".",
    "en": "Use \"Call Of Duty\"'s template."
}

template_help_dark = {
    "fr": "Utilise la template \"dark\".",
    "en": "Use \"dark\" template."
}

template_help_python = {
    "fr": "Utilise la template \"Python\".",
    "en": "Use \"Python\" template."
}

template_help_js = {
    "fr": "Utilise la template \"JavaScript\".",
    "en": "Use \"JavaScript\" template."
}

template_help_omori = {
    "fr": "Utilise la template \"Omori\".",
    "en": "Use \"Omori\" template."
}

template_help_car = {
    "fr": "Utilise la template \"Car\".",
    "en": "Use \"Car\" template."
}

template_help_self = {
    "fr": "Utilise la template \"Nuclear\".",
    "en": "Use \"Nuclear\" template."
}

template_help_webdeck = {
    "fr": "Utilise la template \"WebDeck\".",
    "en": "Use \"WebDeck\" template."
}

template_help_hi = {
    "fr": "Utilise la template \"Hi !\".",
    "en": "Use \"Hi !\" template."
}

template_help_youtube = {
    "fr": "Utilise la template \"Python\".",
    "en": "Use \"Python\" template."
}

template_help_gta = {
    "fr": "Utilise la template \"GTA VI\".",
    "en": "Use \"GTA VI\" template."
}



rpc_cod_details = {
    "fr": "En attente de mission...",
    "en": "Waiting for a mission..."
}

rpc_cod_state = {
    "fr": "Menu principal",
    "en": "In the main menu"
}


tutorial_rpc = {
    "fr": f""" Pour obtenir une image personnalisé:
  1. Envoyer une image (gif, png...) dans Discord. (dans n'importe quelle salon)
  2. Clique droit et "Copier l'adresse de l'image".
  3. Faites `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/exemple.png`.
  4. Fini !""",
    "en": f""" To get a custom rpc image, you should:
  1. Upload an image (gif, png...) into Discord. (in any channel)
  2. Right Click and "Copy Image Link".
  3. Do `{config_selfbot.prefix}rpc_image mp:attachements/67484738743874387438/657438923487543/example.png`.
  4. Done !"""
}