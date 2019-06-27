from pyrez.enumerations import Format, Endpoint, Language
from pyrez.exceptions import PlayerNotFound
from pyrez.models import MOTD
from pyrez.models.Smite import God, GodSkin, Item as SmiteItem, Player as SmitePlayer, TopMatch as SmiteTopMatch, GodRecommendedItem
from pyrez.models.Smite.Team import Player as TeamPlayer, Search as TeamSearch, Info as TeamDetail

from .BaseSmitePaladins import BaseSmitePaladins
from .APIBase import ASYNC
class SmiteAPI(BaseSmitePaladins):
    """Represents a client that connects to |SMITEGAME| API.

    NOTE
    ----
        |PrivacyMode|

    Keyword Arguments
    -----------------
    devId : |INT|
        |DevIdConstruct|
    authKey : |STR|
        |AuthKeyConstruct|
    response_format : Optional :class:`.Format`
        |FormatConstruct|
    sessionId : Optional |STR|
        Manually sets an active sessionId. Passing in ``None`` or an invalid sessionId will use the default instead of the passed in value.
    storeSession : Optional |BOOL|
        Allows Pyrez to read and store sessionId in a .json file. Defaults to ``False``.

    Raises
    ------
    pyrez.exceptions.IdOrAuthEmpty
        Raised when the ``Developer ID`` or ``Authentication Key`` is not specified.
    pyrez.exceptions.InvalidArgument
        Raised when an invalid ``Credentials`` is passed.

    Attributes
    ----------
    authKey
        |AuthKeyAtrib|
    devId
        |DevIdAtrib|
    onSessionCreated
        :class:`pyrez.events.Event` – A decorator that registers an event to listen to.
    response_format:
        |FormatAtrib|
    sessionId
        |STR| – The active sessionId.
    statusPage
        :class:`.StatusPageAPI` – An object that represents :class:`.StatusPageAPI` client.
    storeSession
        |BOOL| – Allows Pyrez to read and store sessionId in a .json file.
    """
    if ASYNC:
        @classmethod
        def Async(cls, devId, authKey, *, response_format=Format.JSON, sessionId=None, storeSession=True, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, loop=None):
            return cls(devId=devId, authKey=authKey, response_format=response_format, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=True, loop=loop)
    def __init__(self, devId, authKey, *, response_format=Format.JSON, sessionId=None, storeSession=True, headers=None, cookies=None, raise_for_status=True, logger_name=None, debug_mode=True, is_async=False, loop=None):
        super().__init__(devId=devId, authKey=authKey, endpoint=Endpoint.SMITE, response_format=response_format, sessionId=sessionId, storeSession=storeSession, headers=headers, cookies=cookies, raise_for_status=raise_for_status, logger_name=logger_name, debug_mode=debug_mode, is_async=is_async, loop=loop)

    # GET /getgods[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
    def getGods(self, language=Language.English):
        """Returns all Gods and their various attributes.

        Parameters
        ----------
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.

        Returns
        -------
            List of pyrez.models.God or pyrez.models.Champion objects
        """
        return self.__request_method__('getgods', God, 1, params=[language or Language.English])

    # GET /getgodrecommendeditems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
    def getGodRecommendedItems(self, godId, language=Language.English):
        """Returns the Recommended Items for a particular God.

        Parameters
        ----------
        godId : |INT|
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getgodrecommendeditems', GodSGodRecommendedItemkin, 1, params=[godId, language or Language.English])

    # GET /getgodskins[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{godId}/{languageCode}
    def getGodSkins(self, godId, language=Language.English):
        """Returns all available skins for a particular God.

        Parameters
        ----------
        godId : |INT|
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorB|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getgodskins', GodSkin, 1, params=[godId, language or Language.English])

    # GET /getitems[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{languageCode}
    def getItems(self, language=Language.English):
        """Returns all Items and their various attributes.

        Parameters
        ----------
        language : |LanguageParam|
            |LanguageParamDescrip|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getitems', SmiteItem, 1, params=[language or Language.English])

    # GET /getmotd[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getMotd(self):
        """Returns information about the 20 most recent Match-of-the-Days.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getmotd', MOTD, 1)

    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}
    # GET /getplayer[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{playerIdOrName}/{portalId}
    def getPlayer(self, player, portalId=None):
        return self.__request_method__('getplayer', SmitePlayer, 1, params=[player, portalId] if portalId else [player], raises=PlayerNotFound("Player don't exist or it's hidden"))

    # GET /getteamdetails[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{clanId}
    def getTeamDetails(self, clanId):
        """Lists the number of players and other high level details for a particular clan.

        Parameters
        ----------
        clanId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getteamdetails', TeamDetail, 1, params=[clanId])

    # GET /getteamplayers[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{clanId}
    def getTeamPlayers(self, clanId):
        """Lists the players for a particular clan.

        Parameters
        ----------
        clanId : |INT|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('getteamplayers', TeamPlayer, 1, params=[clanId])

    # GET /gettopmatches[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}
    def getTopMatches(self):
        """Lists the 50 most watched / most recent recorded matches.

        Raises
        ------
        TypeError
            |TypeError|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('gettopmatches', SmiteTopMatch, 1)

    # GET /searchteams[ResponseFormat]/{devId}/{signature}/{sessionId}/{timestamp}/{searchTeam}
    def searchTeams(self, searchTeam):
        """Returns high level information for Clan names containing the ``searchTeam`` string.

        Parameters
        ----------
        searchTeam : |STR|

        Raises
        ------
        TypeError
            |TypeErrorA|

        NOTE
        ----
            This method raises :meth:`makeRequest` exceptions.
        """
        return self.__request_method__('searchteams', TeamSearch, 1, params=[searchTeam])
