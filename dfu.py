# "D"ata "F"ile for needed "U"sage = dfu -----> strings, constants etc.

str_start = "\n\n\n * * * * * * * * * * * * START * * * * * * * * * * * * * "

str_time_out = "Timed out, NOT logged, {:%d.%m.%Y %H:%M:%S}"

str_idx_err = (
                "Index Error: no messages on Telegram "
                "server(?). NOT logged, {:%d.%m.%Y %H:%M:%S}"
                )
lst_str_hlp_cmd = [ # 'who', 'what', 'why', 'how', 'where',
                     '.*\?', 'info', '/info', '/commands', 'commands',
                     '/help', '--help', '-help', 'help']

lst_str_hom_cmd = ['/home', 'home']
lst_str_wrk_cmd = ['/work', 'work']
lst_str_upd_hom_cmd = ['home=', 'home =']
lst_str_upd_wrk_cmd = ['work=', 'work =']
lst_str_upd_nam_cmd = ['name=', 'name =']
# lst_str_to_cmd = [' to ', '--']
str_to_opr = ' to '

str_out_cmnds = (
                 "<b>work</b> (Calc route from home to work)\n"
                 "<b>home</b> (.. to HOME)\n"
                 "<b>work=Ben Gurion 5, Holon</b> (set work address)\n"
                 "<b>home=haifa, Hertzl 156</b> (set HOME address)\n"
                 "<b>name=Zvika</b> (set name)\n"
                 )
str_per_dtl = "\ncurrent home: {}\ncur work: {}\n"

b_s = '<b>'
b_e = '</b>'

# daily_rt_scdl_hh_str = '14'       # 15:mm   # strftime('%H:%M') ~"2018-11-07 11:57:53.238483~
# daily_rt_scdl_mm_max_str = '45'   # HH:45
#
# tm_sample_delta_hh = 0
# tm_sample_delta_mm = 1
# tm_sample_delta_ss = 15
#
# rt_tm_long = 40


str_greeting = (
                "hello {} iam a mishkas robot  **{}**, your "
                "msg=`{}`, type  `info`  to get commands list"
                )

# str_full_tm_dist = "({}) FROM:   {}\nTO:   {}\n*** Time: {:.0f} min ({:.0f} km)"      #%.2f
str_full_tm_dist = "({}) FROM:   {}\nTO:   {}"      #%.2f


dict_heb_chr_u8_ucode = {
                        # u'\x93':u'\u05D3',
                        # u'\xa8':u'\u05E8',
                        u'\x90':u'\u05D0',
                        u'\x91':u'\u05D1',
                        u'\x92':u'\u05D2',
                        u'\x93':u'\u05D3',
                        u'\x94':u'\u05D4',
                        u'\x95':u'\u05D5',
                        u'\x96':u'\u05D6',
                        u'\x97':u'\u05D7',
                        u'\x98':u'\u05D8',
                        u'\x99':u'\u05D9',
                        u'\x9a':u'\u05DA',
                        u'\x9b':u'\u05DB',
                        u'\x9c':u'\u05DC',
                        u'\x9d':u'\u05DD',
                        u'\x9e':u'\u05DE',
                        u'\x9f':u'\u05DF',
                        u'\xa0':u'\u05E0',
                        u'\xa1':u'\u05E1',
                        u'\xa2':u'\u05E2',
                        u'\xa3':u'\u05E3',
                        u'\xa4':u'\u05E4',
                        u'\xa5':u'\u05E5',
                        u'\xa6':u'\u05E6',
                        u'\xa7':u'\u05E7',
                        u'\xa8':u'\u05E8',
                        u'\xa9':u'\u05E9',
                        u'\xaa':u'\u05EA'
                        }







"""

# search "comands strings" in input message:
        # if re.compile('|'.join(dfu.lst_str_in_cmd_hom + dfu.lst_str_in_cmd_wrk),
        #               re.IGNORECASE).search(self.anlz_msg_txt):




# str_is_cur_msg = "cur message: msg_id={}, chat_id={}, text={}, Name={}"
# str_wz_srch_lst = ['wz','waz','waze']
# from_address = tokenbot.from_address_main
# to_address = tokenbot.to_address_main
# region = 'IL'

    # def chk_auth(self):
    #     if self.anlz_msg_cht_id in tokenbot.hi_auth_id_lst:
    #             self.msg_prs_hi_auth_id = True

#
# str_rsrv_struct = (
#                     "reservation structure:\n"
#                     "Source \n"
#                     "dd.mm.yy  HH:MM \n"
#                     "Dest \n"
#                     "timing always between Source and Dest - so one of the"
#                     "directions is NON-obligatory!"
#                     )
#
# str_qstn_rule_y = (
#                     "serving  MATAF TAXI reservations, type `info` for "
#                     "reservation instructions, "
#                     )


# str_qstn_rule_gen = "type `info` for reservation instructions, `wz` to get HOME:] "




# str_in_cmd_pause = 'pause'

        # "pause comp_name":
        # elif (self.anlz_msg_txt.lower().startswith(dfu.str_in_cmd_pause) and
        #       len(self.anlz_msg_txt.lower().split(' ')) == 2):
        #     if self.anlz_msg_txt.lower().split(' ')[1] == platform.node():
        #         self.chk_auth()
        #         if self.msg_prs_hi_auth_id:
        #             self.cre_msg_txt_new += '\n* * * P A U S E * * *'
        # help/commands/info~:

https://www.utf8-chartable.de/unicode-utf8-table.pl?start=1408&number=128&utf8=string-literal

u'\x90':u'u\05D0',
u'\x91':u'u\05D1',
u'\x92':u'u\05D2',
u'\x93':u'u\05D3',
u'\x94':u'u\05D4',
u'\x95':u'u\05D5',
u'\x96':u'u\05D6',
u'\x97':u'u\05D7',
u'\x98':u'u\05D8',
u'\x99':u'u\05D9',
u'\x9a':u'u\05DA',
u'\x9b':u'u\05DB',
u'\x9c':u'u\05DC',
u'\x9d':u'u\05DD',
u'\x9e':u'u\05DE',
u'\x9f':u'u\05DF',
u'\xa0':u'u\05E0',
u'\xa1':u'u\05E1',
u'\xa2':u'u\05E2',
u'\xa3':u'u\05E3',
u'\xa4':u'u\05E4',
u'\xa5':u'u\05E5',
u'\xa6':u'u\05E6',
u'\xa7':u'u\05E7',
u'\xa8':u'u\05E8',
u'\xa9':u'u\05E9',
u'\xaa':u'u\05EA'


U+05D0		\xd7\x90	HEBREW LETTER ALEF
U+05D1		\xd7\x91	HEBREW LETTER BET
U+05D2		\xd7\x92	HEBREW LETTER GIMEL
U+05D3		\xd7\x93	HEBREW LETTER DALET
U+05D4		\xd7\x94	HEBREW LETTER HE
U+05D5		\xd7\x95	HEBREW LETTER VAV
U+05D6		\xd7\x96	HEBREW LETTER ZAYIN
U+05D7		\xd7\x97	HEBREW LETTER HET
U+05D8		\xd7\x98	HEBREW LETTER TET
U+05D9		\xd7\x99	HEBREW LETTER YOD
U+05DA		\xd7\x9a	HEBREW LETTER FINAL KAF
U+05DB		\xd7\x9b	HEBREW LETTER KAF
U+05DC		\xd7\x9c	HEBREW LETTER LAMED
U+05DD		\xd7\x9d	HEBREW LETTER FINAL MEM
U+05DE		\xd7\x9e	HEBREW LETTER MEM
U+05DF		\xd7\x9f	HEBREW LETTER FINAL NUN
U+05E0		\xd7\xa0	HEBREW LETTER NUN
U+05E1		\xd7\xa1	HEBREW LETTER SAMEKH
U+05E2		\xd7\xa2	HEBREW LETTER AYIN
U+05E3		\xd7\xa3	HEBREW LETTER FINAL PE
U+05E4		\xd7\xa4	HEBREW LETTER PE
U+05E5		\xd7\xa5	HEBREW LETTER FINAL TSADI
U+05E6		\xd7\xa6	HEBREW LETTER TSADI
U+05E7		\xd7\xa7	HEBREW LETTER QOF
U+05E8		\xd7\xa8	HEBREW LETTER RESH
U+05E9		\xd7\xa9	HEBREW LETTER SHIN
U+05EA		\xd7\xaa	HEBREW LETTER TAV

print r.lst_msg ---> gives only 'visible' parts of CLASS:
{'delete_chat_photo': False, 'new_chat_photo': [],
'from': {'first_name': u'Zevik', 'last_name': u'Hertzl', 'is_bot': False, 'id': 672748593, 'language_code': u'en-IL'},
'text': u'R', 'caption_entities': [], 'entities': [], 'channel_chat_created': False, 'new_chat_members': [],
'supergroup_chat_created': False,
 'chat': {'first_name': u'Zevik', 'last_name': u'Hertzl', 'type': u'private','id': 672748593},
 'photo': [], 'date': 1542174651, 'group_chat_created': False, 'message_id': 2034}

type(r.lst_msg) =   <class 'telegram.message.Message'>


dir(r.lst_msg) =

['ATTACHMENT_TYPES', 'MESSAGE_TYPES', '__abstractmethods__', '__class__', '__delattr__', '__dict__',
 '__doc__', '__eq__', '__format__', '__getattribute__', '__getitem__', '__hash__', '__init__', '__metaclass__',
  '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
   '__subclasshook__', '__weakref__', '_abc_cache', '_abc_negative_cache', '_abc_negative_cache_version',
   '_abc_registry', '_effective_attachment', '_id_attrs', '_parse_html', '_parse_markdown', '_quote',

    'audio',
   'author_signature', 'bot', 'caption', 'caption_entities', 'caption_html', 'caption_html_urled', 'caption_markdown',
   'caption_markdown_urled', 'channel_chat_created',
   'chat',
    'chat_id', 'connected_website', 'contact', 'date',
    'de_json', 'delete', 'delete_chat_photo', 'document', 'edit_caption', 'edit_date', 'edit_reply_markup',
    'edit_text', 'effective_attachment', 'entities', 'forward', 'forward_date', 'forward_from', 'forward_from_chat',
    'forward_from_message_id', 'forward_signature', 'from_user', 'game', 'group_chat_created', 'invoice',
    'left_chat_member', 'location', 'media_group_id', 'message_id', 'migrate_from_chat_id', 'migrate_to_chat_id',
     'new_chat_members', 'new_chat_photo', 'new_chat_title', 'parse_caption_entities', 'parse_caption_entity',
     'parse_entities', 'parse_entity', 'photo', 'pinned_message', 'reply_audio', 'reply_contact', 'reply_document',
      'reply_html', 'reply_location', 'reply_markdown', 'reply_media_group', 'reply_photo', 'reply_sticker',
      'reply_text', 'reply_to_message', 'reply_venue', 'reply_video', 'reply_video_note', 'reply_voice',
       'sticker', 'successful_payment', 'supergroup_chat_created', 'text', 'text_html', 'text_html_urled',
       'text_markdown', 'text_markdown_urled', 'to_dict', 'to_json', 'venue', 'video', 'video_note', 'voice']



"""