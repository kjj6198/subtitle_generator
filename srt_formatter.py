from math import floor


def _pad(num, pad_num=2):
    if (pad_num is 2):
        return "{:02d}".format(int(num))
    else:
        return "{:03d}".format(int(num))


def format_srt(transcripts, outfile=""):
    with open(outfile, "a") as file:
        for (i, t) in enumerate(transcripts):
            # start time
            sh = _pad(t["start_time"] // 3600)
            sm = _pad(floor(t["start_time"] % 3600 / 60))
            ss = _pad(floor(t["start_time"] % 60))
            smf = _pad(floor(t["start_time"] * 1000) % 1000, pad_num=3)
            # end time
            eh = _pad(t["end_time"] // 3600)
            em = _pad(floor(t["end_time"] % 3600 / 60))
            es = _pad(floor(t["end_time"] % 60))
            esf = _pad(floor(t["end_time"] * 1000) % 1000, pad_num=3)

            file.writelines([
                "{}\n".format(i+1),
                "{h}:{m}:{s},{sms} --> {eh}:{em}:{es},{ems}\n".format(
                    h=sh, m=sm, s=ss, sms=smf,
                    eh=eh, em=em, es=es, ems=esf
                ),
                "{text}\n\n".format(text=t["text"])
            ])
