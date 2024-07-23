import json

from pymongo import MongoClient

from ubot.config import DB_NAME, MONGO_URL

# from ubot.core.database.afkdb import *


################################################################
"""
 YANG PAKE KODE INI TERUS JILAT LUDAH SENDIRI GUA DO'A IN ANAK LU CACAT TUJUH TURUNAN, BADAN LU BELATUNG ISI NYA 
 
 @ CREDIT : NAN-DEV
"""
################################################################


class MongoDB:
    def __init__(self, db_name, mongo_url: str) -> None:
        self._db = MongoClient(mongo_url)
        self._db = self._db[db_name]
    
    def cek_userdata(self, user_id: int) -> bool:
        user = self._db.matadb.find_one({"user_id": user_id})
        return bool(user)

    def get_userdata(self, user_id: int) -> bool:
        user = self._db.matadb.find_one({"user_id": user_id})
        return user

    def add_userdata(self, user_id: int, depan, belakang, username, mention, full, _id):
        self._db.matadb.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "depan": depan,
                    "belakang": belakang,
                    "username": username,
                    "mention": mention,
                    "full": full,
                    "_id": _id,
                }
            },
            upsert=True,
        )

    def get_flood(self, gw, user_id):
        user = self._db.floods.find_one({"gw": gw, "user_id": user_id})
        if user:
            return user.get("flood")
        else:
            return None

    def set_flood(self, gw, user_id, flood):
        self._db.floods.update_one(
            {"gw": gw, "user_id": user_id}, {"$set": {"flood": flood}}, upsert=True
        )

    def rem_flood(self, gw, user_id):
        self._db.floods.delete_one({"gw": gw, "user_id": user_id})
    
    def save_text_sch(self, user_id, text_sch_name, text_sch_data, msg_type, file=None):
        schdb = self._db.schdbnew

        schdb.update_one(
            {"user_id": user_id, "text_sch_name": text_sch_name},
            {
                "$set": {
                    "text_sch_data": text_sch_data,
                    "msg_type": msg_type,
                    "file": file,
                }
            },
            upsert=True,
        )

    def get_text_sch(self, user_id, text_sch_name):
        schdb = self._db.schdbnew

        result = schdb.find_one(
            {"user_id": user_id, "text_sch_name": text_sch_name},
            {"_id": 0, "text_sch_data": 1, "msg_type": 1, "file": 1},
        )

        if result:
            return {
                "value": result.get("text_sch_data"),
                "type": result.get("msg_type"),
                "file": result.get("file"),
            }

    def get_all_text_schs(self, user_id):
        schdb = self._db.schdbnew

        result = schdb.find({"user_id": user_id}, {"_id": 0, "text_sch_name": 1})

        return (
            [item.get("text_sch_name") for item in result if "text_sch_name" in item]
            if result
            else []
        )

    def rm_text_sch(self, user_id, text_sch_name):
        schdb = self._db.schdbnew

        schdb.delete_one({"user_id": user_id, "text_sch_name": text_sch_name})

    def add_sch(self, user_id, chat_id):
        schdb = self._db.schdbnew
        seks = schdb.find_one({"user_id": user_id, "chat_id": chat_id})
        if not seks:
            return schdb.insert_one({"user_id": user_id, "chat_id": chat_id})

    def del_sch(self, user_id, chat_id):
        schdb = self._db.schdbnew
        seks = schdb.find_one({"user_id": user_id, "chat_id": chat_id})
        if seks:
            return schdb.delete_one({"user_id": user_id, "chat_id": chat_id})

    def list_sch(self, user_id):
        schdb = self._db.schdbnew
        sch_lists = []
        for ze in schdb.find({"user_id": user_id, "chat_id": {"$lt": 0}}):
            sch_lists.append(ze["chat_id"])
        return sch_lists

    def add_ubot(self, user_id, api_id, api_hash, session_string):
        ubotdb = self._db.ubotdb

        ubotdb.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "api_id": api_id,
                    "api_hash": api_hash,
                    "session_string": session_string,
                }
            },
            upsert=True,
        )

    def remove_ubot(self, user_id):
        ubotdb = self._db.ubotdb

        ubotdb.delete_one({"user_id": user_id})

    def get_userbots(self):
        ubotdb = self._db.ubotdb
        data = ubotdb.find({"user_id": {"$exists": 1}}, {"_id": 0})
        return [
            {
                "name": str(ubot["user_id"]),
                "api_id": ubot["api_id"],
                "api_hash": ubot["api_hash"],
                "session_string": ubot["session_string"],
            }
            for ubot in data
        ]

    def get_pref(self, user_id):
        user_prefixes = self._db.user_prefixes

        result = user_prefixes.find_one({"user_id": user_id}, {"_id": 0, "prefix": 1})

        return json.loads(result["prefix"]) if result and "prefix" in result else "."

    def set_pref(self, user_id, prefix):
        user_prefixes = self._db.user_prefixes

        user_prefixes.update_one(
            {"user_id": user_id}, {"$set": {"prefix": json.dumps(prefix)}}, upsert=True
        )

    def rem_pref(self, user_id):
        user_prefixes = self._db.user_prefixes

        user_prefixes.delete_one({"user_id": user_id})

    def set_var(self, bot_id, vars_name, value, query="vars"):
        update_data = {"$set": {f"{query}.{vars_name}": value}}

        self._db.vardb.update_one({"_id": bot_id}, update_data, upsert=True)

    def get_var(self, bot_id, vars_name, query="vars"):
        document = self._db.vardb.find_one({"_id": bot_id})
        return document.get(query, {}).get(vars_name, None) if document else None

    def remove_var(self, bot_id, vars_name, query="vars"):
        hapus_data = {"$unset": {f"{query}.{vars_name}": ""}}
        self._db.vardb.update_one({"_id": bot_id}, hapus_data)

    def all_var(self, user_id, query="vars"):
        documents = self._db.vardb.find({"_id": user_id})
        return [json.loads(doc["value"]) for doc in documents] if documents else None

    def remove_all_var(self, bot_id):
        self._db.vardb.delete_many({"bot_id": bot_id})

    def rm_all(self, bot_id):
        self._db.vardb.delete_many({"bot_id": bot_id})

    def get_list_from_var(self, user_id, vars_name, query="vars"):
        vars_data = self.get_var(user_id, vars_name, query)
        return [int(x) for x in str(vars_data).split()] if vars_data else []

    def add_to_var(self, user_id, vars_name, value, query="vars"):
        vars_list = self.get_list_from_var(user_id, vars_name, query)
        vars_list.append(value)
        self.set_var(user_id, vars_name, " ".join(map(str, vars_list)), query)

    def remove_from_var(self, user_id, vars_name, value, query="vars"):
        vars_list = self.get_list_from_var(user_id, vars_name, query)
        if value in vars_list:
            vars_list.remove(value)
            self.set_var(user_id, vars_name, " ".join(map(str, vars_list)), query)

    # def set_var(self, orang, nama_var, value):
    # update_data = {"$set": {f"{orang}.{nama_var}": value}}
    # self._db.vardb.update_one({"_id": orang}, update_data, upsert=True)

    # def get_var(self, orang, nama_var):
    # document = self._db.vardb.find_one({"_id": f"{orang}.{nama_var}"})
    # return document if document and document else None

    # def rem_all_var(self, bot_id):
    # self._db.vardb.delete_one({"orang": bot_id})

    # def remove_var(self, orang, nama_var):
    # self._db.vardb.delete_one({"_id": f"{orang}.{nama_var}"})

    def oke_pc(self, user_id):
        good_usr = int(user_id)
        ada_ga = self._db.permitdb.find_one({"user_id": "setujui"})
        if ada_ga:
            self._db.permitdb.update_one(
                {"user_id": "setujui"}, {"$push": {"good_id": good_usr}}
            )
        else:
            self._db.permitdb.insert_one({"user_id": "setujui", "good_id": [good_usr]})

    def tolak_pc(self, user_id):
        bad_usr = int(user_id)
        ada_ga = self._db.permitdb.find_one({"user_id": "setujui"})
        if ada_ga:
            self._db.permitdb.update_one(
                {"user_id": "setujui"}, {"$pull": {"good_id": bad_usr}}
            )
        else:
            return None

    def dicek_pc(self, user_id):
        random_usr = int(user_id)
        ada_ga = self._db.permitdb.find_one({"user_id": "setujui"})
        if ada_ga:
            ad_org = [ok_org for ok_org in ada_ga.get("good_id")]
            if random_usr in ad_org:
                return True
            else:
                return False
        else:
            return False

    def ambil_jumlah_kata(self):
        katagikes = self._db.katagikes

        orang_nya = katagikes.count_documents({"orang": {"$lt": 0}})
        kata_nya = sum(
            len(row["katax"].split()) if row["katax"] else 0
            for row in katagikes.find({"orang": {"$lt": 0}}, {"_id": 0, "katax": 1})
        )

        return {
            "orang_nya": orang_nya,
            "kata_nya": kata_nya,
        }

    def ambil_daftar(self, orang):
        katagikes = self._db.katagikes

        result = katagikes.find_one({"orang": orang}, {"_id": 0, "katax": 1})

        if result and result.get("katax"):
            try:
                return json.loads(result["katax"])
            except json.JSONDecodeError:
                return []
        else:
            return []

    def tambah_kata(self, orang, kalimat):
        katagikes = self._db.katagikes

        katax = self.ambil_daftar(orang)
        if not isinstance(katax, list):
            katax = []

        kalimat = kalimat.strip()
        katax.append(kalimat)

        katagikes.update_one(
            {"orang": orang}, {"$set": {"katax": json.dumps(katax)}}, upsert=True
        )

    def kureng_kata(self, orang, kata):
        katagikes = self._db.katagikes

        result = katagikes.find_one({"orang": orang}, {"_id": 0, "katax": 1})

        if result and result.get("katax"):
            kataxd = json.loads(result["katax"])
            if kata in kataxd:
                kataxd.remove(kata)

                katagikes.update_one(
                    {"orang": orang}, {"$set": {"katax": json.dumps(kataxd)}}
                )

                return True

        return False

    def save_note(self, user_id, note_name, note_data, msg_type, file=None):
        selfnotes = self._db.selfnotes

        selfnotes.update_one(
            {"user_id": user_id, "note_name": note_name},
            {"$set": {"note_data": note_data, "msg_type": msg_type, "file": file}},
            upsert=True,
        )

    def get_note(self, user_id, note_name):
        selfnotes = self._db.selfnotes

        result = selfnotes.find_one(
            {"user_id": user_id, "note_name": note_name},
            {"_id": 0, "note_data": 1, "msg_type": 1, "file": 1},
        )

        if result:
            return {
                "value": result.get("note_data"),
                "type": result.get("msg_type"),
                "file": result.get("file"),
            }

    def get_all_notes(self, user_id):
        selfnotes = self._db.selfnotes

        result = selfnotes.find({"user_id": user_id}, {"_id": 0, "note_name": 1})

        return [item["note_name"] for item in result] if result else []

    def get_all_notes_inline(self, user_id):
        selfnotes = self._db.selfnotes

        result = selfnotes.find(
            {"user_id": user_id},
            {"_id": 0, "note_name": 1, "note_data": 1, "msg_type": 1, "file": 1},
        )

        allnotes = {}
        for item in result:
            allnotes[item["note_name"]] = {
                "value": item.get("note_data"),
                "type": item.get("msg_type"),
                "file": item.get("file"),
            }

        return allnotes

    def rm_note(self, user_id, note_name):
        selfnotes = self._db.selfnotes

        selfnotes.delete_one({"user_id": user_id, "note_name": note_name})

    def get_two_factor(self, user_id):
        result = self._db.twofactor.find_one(
            {"user_id": user_id}, {"_id": 0, "value": 1}
        )

        return result.get("value") if result and "value" in result else None

    def set_two_factor(self, user_id, twofactor):
        self._db.twofactor.update_one(
            {"user_id": user_id}, {"$set": {"value": twofactor}}, upsert=True
        )

    def get_log_group(self, user_id):
        log_groups = self._db.log_groups

        result = log_groups.find_one({"user_id": user_id}, {"_id": 0, "logger": 1})

        return result.get("logger") if result and "logger" in result else None

    def set_log_group(self, user_id, logger):
        log_groups = self._db.log_groups

        log_groups.update_one(
            {"user_id": user_id}, {"$set": {"logger": logger}}, upsert=True
        )

    def del_log_group(self, user_id):
        log_groups = self._db.log_groups

        log_groups.delete_one({"user_id": user_id})

    def rem_two_factor(self, user_id):
        self._db.twofactor.update_one(
            {"user_id": user_id}, {"$set": {"value": ""}}, upsert=True
        )

    def get_chat(self, user_id):
        blocked_chats = self._db.blocked_chats

        result = blocked_chats.find_one({"user_id": user_id}, {"_id": 0, "chat_id": 1})

        return json.loads(result["chat_id"]) if result and "chat_id" in result else []

    def add_chat(self, user_id, chat_id):
        blocked_chats = self._db.blocked_chats

        current_list = self.get_chat(user_id)
        current_list.append(chat_id)

        blocked_chats.update_one(
            {"user_id": user_id},
            {"$set": {"chat_id": json.dumps(current_list)}},
            upsert=True,
        )
        return True

    def remove_chat(self, user_id, chat_id):
        blocked_chats = self._db.blocked_chats

        current_list = self.get_chat(user_id)
        current_list.remove(chat_id)

        blocked_chats.update_one(
            {"user_id": user_id}, {"$set": {"chat_id": json.dumps(current_list)}}
        )
        return True

    def ambil_spgc(self, user_id):
        spam_gc = self._db.spam_gc

        result = spam_gc.find_one({"user_id": user_id}, {"_id": 0, "chat_id": 1})

        return json.loads(result["chat_id"]) if result and "chat_id" in result else []

    def tambah_spgc(self, user_id, chat_id):
        spam_gc = self._db.spam_gc

        current_list = self.ambil_spgc(user_id)
        current_list.append(chat_id)

        spam_gc.update_one(
            {"user_id": user_id},
            {"$set": {"chat_id": json.dumps(current_list)}},
            upsert=True,
        )
        return True

    def kureng_spgc(self, user_id, chat_id):
        spam_gc = self._db.spam_gc

        current_list = self.ambil_spgc(user_id)
        current_list.remove(chat_id)

        spam_gc.update_one(
            {"user_id": user_id}, {"$set": {"chat_id": json.dumps(current_list)}}
        )
        return True

    def ambil_spdb(self, user_id):
        spam_db = self._db.spam_db

        result = spam_db.find_one({"user_id": user_id}, {"_id": 0, "chat_id": 1})

        return json.loads(result["chat_id"]) if result and "chat_id" in result else []

    def tambah_spdb(self, user_id, chat_id):
        spam_db = self._db.spam_db

        current_list = self.ambil_spdb(user_id)
        current_list.append(chat_id)

        spam_db.update_one(
            {"user_id": user_id},
            {"$set": {"chat_id": json.dumps(current_list)}},
            upsert=True,
        )
        return True

    def kureng_spdb(self, user_id, chat_id):
        spam_db = self._db.spam_db

        current_list = self.ambil_spdb(user_id)
        current_list.remove(chat_id)

        spam_db.update_one(
            {"user_id": user_id}, {"$set": {"chat_id": json.dumps(current_list)}}
        )
        return True

    def get_prem(self):
        sudoers = self._db.sudoers

        result = sudoers.find({}, {"_id": 0, "user_id": 1})

        return [item["user_id"] for item in result] if result else []

    def cek_prem(self, user_id):
        sudoers = self._db.sudoers

        result = sudoers.find_one({"user_id": user_id}, {"_id": 0, "user_id": 1})

        return result

    def add_prem(self, user_id):
        sudoers = self._db.sudoers

        sudoers.update_one(
            {"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True
        )
        return True

    def remove_prem_all(self):
        sudoers = self._db.sudoers

        sudoers.delete_many({"user_id": "user_id"})
        return True

    def remove_prem(self, user_id):
        sudoers = self._db.sudoers

        sudoers.delete_one({"user_id": user_id})
        return True

    def get_seles(self):
        resellers = self._db.resellers

        result = resellers.find({}, {"_id": 0, "user_id": 1})

        return [item["user_id"] for item in result] if result else []

    def cek_seles(self, user_id):
        resellers = self._db.resellers

        result = resellers.find_one({"user_id": user_id}, {"_id": 0, "user_id": 1})

        return result

    def add_seles(self, user_id):
        resellers = self._db.resellers

        resellers.update_one(
            {"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True
        )
        return True

    def remove_seles(self, user_id):
        resellers = self._db.resellers

        resellers.delete_one({"user_id": user_id})
        return True

    def remove_seles_all(self):
        resellers = self._db.resellers

        resellers.delete_many({"user_id": "user_id"})
        return True

    def get_expired_date(self, user_id):
        user = self._db.users.find_one({"_id": user_id})
        if user:
            return user.get("expire_date")
        else:
            return None

    def set_expired_date(self, user_id, expire_date):
        self._db.users.update_one(
            {"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True
        )

    def rem_expired_date(self, user_id):
        self._db.users.update_one(
            {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
        )

    def is_served_user(self, user_id):
        served_users = self._db.served_users

        result = served_users.find_one({"user_id": user_id}, {"_id": 0, "user_id": 1})

        return result is not None

    def get_served_users(self):
        served_users = self._db.served_users

        result = served_users.find({}, {"_id": 0, "user_id": 1})

        return [item["user_id"] for item in result] if result else []

    def add_served_user(self, user_id):
        served_users = self._db.served_users

        served_users.update_one(
            {"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True
        )


monggo_uri = MONGO_URL
monggo = MongoDB(db_name=DB_NAME, mongo_url=monggo_uri)
