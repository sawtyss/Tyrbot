from core.command_param_types import Options
from core.decorators import instance, command
from core.tyrbot import Tyrbot


@instance()
class LangController:

    def inject(self, registry):
        self.ts = registry.get_instance("translation_service")
        self.bot: Tyrbot = registry.get_instance("bot")

    @command(command="lang", params=[Options(["de_DE", "en_US"])], description="Changes the language of the bot",
             access_level="moderator", sub_command="set")
    def reload_translation(self, request, lang):
        self.ts.reload_translation(lang)
        return "<orange>Language changed to <highlight>{lang}<end> <end>".format(lang=lang)


    @command(command="lang", params=[], description="Gets the language of the bot", access_level="all")
    def print_lang(self, _):
        return "My current language is <highlight>{lang}<end>".format(lang=self.ts.language)
