logs_column_descriptions = {
    "prp": {
        "sub_id": {
            "LongName": "Participant ID",
            "Description": "Subject identifier",
        },
        "task": {
            "LongName": "Task",
            "Description": "Task this log file corresponds to",
            "Levels": {
                "prp": "prp task"
            }
        },
        "is_practice": {
            "LongName": "Is practice",
            "Description": "Task is practice or actual experiment",
            "Levels": {
                0: "Not practice",
                1: "Practice"
            }
        },
        "Block": {
            "LongName": "Block number",
            "Description": "Block number of this trial. At the beginning of each block, a new target pair is presented",
            "Units": "a.u."
        },
        "Trial": {
            "LongName": "Trial number",
            "Description": "Number of the trial within this block",
            "Units": "a.u."
        },
        "target_01": {
            "LongName": "First visual target",
            "Description": "Name of the first target stimulus",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities",
            }
        },
        "target_02": {
            "LongName": "Second visual target",
            "Description": "Name of the second target stimulus",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities"
            }
        },
        "task_relevance": {
            "LongName": "Task relevance",
            "Description": "Task relevance of the stimulus presented in this trial",
            "Levels": {
                "non-target": "Stimulus of the same category but different identity than the targets",
                "irrelevant": "Stimulus of a different category than the targets",
                "target": "Same stimulus identity as targets"
            }
        },
        "category": {
            "LongName": "Category",
            "Description": "Category of the presented stimulus",
            "Levels": {
                "face": "Face stimulus",
                "object": "Object stimulus",
                "letter": "Letter stimulus",
                "false": "False stimulus"
            }
        },
        "orientation": {
            "LongName": "Orientation",
            "Description": "Orientation of the presented stimulus",
            "Levels": {
                "center": "Center facing stimulus",
                "left": "Left (-30°) facing stimulus",
                "right": "Right (30°) facing stimulus"
            }
        },
        "duration": {
            "LongName": "Duration",
            "Description": "Duration for which the stimulus remained on the screen",
            "Levels": {
                "0.5": "Stimulus presented for 0.5 seconds",
                "1.0": "Stimulus presented for 1.0 seconds",
                "1.5": "Stimulus presented for 1.5 seconds"
            },
            "Units": "s"
        },
        "stim_jit": {
            "LongName": "Stimulus jitter",
            "Description": "Random jitter added after the current trial, to randomize the next stimulus onset time. The"
                           "jitter was generated from a truncated exponential distribution with mean of 1s",
            "Units": "s"
        },
        "SOA": {
            "LongName": "Stimulus onset asynchrony",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset or offset",
            "Levels": {
                "0.0": "Tone presented at 0s delay from event",
                "0.116": "Tone presented at 0.116s delay from event",
                "0.232": "Tone presented at 0.232s delay from event",
                "0.466": "Tone presented at 0.466s delay from event",
            },
            "Units": "s"
        },
        "onset_SOA": {
            "LongName": "Stimulus onset asynchrony from visual stimulus onset",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset. If the tone is presented "
                           "relative to the stimulus offset, this variable takes the value of column SOA + column "
                           "duration",
            "Levels": {
                "0.0": "Tone presented at 0s delay from T1 onset",
                "0.116": "Tone presented at 0.116s delay from T1 onset",
                "0.232": "Tone presented at 0.232s delay from T1 onset",
                "0.466": "Tone presented at 0.466s delay from T1 onset",
                "0.5": "Tone presented at 0s delay from 0.5 T1 offset",
                "0.616": "Tone presented at 0.116s delay from 0.5 T1 offset",
                "0.732": "Tone presented at 0.232s delay from 0.5 T1 offset",
                "0.966": "Tone presented at 0.466s delay from 0.5 T1 offset",
                "1.0": "Tone presented at 0s delay from 1.0 T1 offset",
                "1.116": "Tone presented at 0.116s delay 1.0 T1 offset",
                "1.232": "Tone presented at 0.232s delay 1.0 T1 offset",
                "1.466": "Tone presented at 0.466s delay 1.0 T1 offset",
                "1.5": "Tone presented at 0s delay from 1.5 T1 offset",
                "1.616": "Tone presented at 0.116s delay 1.5 T1 offset",
                "1.732": "Tone presented at 0.232s delay 1.5 T1 offset",
                "1.966": "Tone presented at 0.466s delay 1.5 T1 offset",
            },
            "Units": "s"
        },
        "SOA_lock": {
            "LongName": "Lock of auditory tone onset asynchrony",
            "Description": "Whether the auditory tone was presented relative to the onset or offset of T1 stimulus",
            "Levels": {
                "onset": "Tone presented relative to T1 onset",
                "offset": "Tone presented relative to T1 offset"
            }
        },
        "pitch": {
            "LongName": "Auditory stimulus (T2) pitch",
            "Description": "Pitch of the auditory stimulus",
            "Levels": {
                "1000": "Low pitch",
                "1100": "High pitch"
            },
            "Units": "Hz"
        },
        "texture": {
            "LongName": "Texture number",
            "Description": "Number of the visual stimulus texture loaded in memory by PTB",
            "Units": "a.u."
        },
        "vis_stim_time": {
            "LongName": "Visual stimulus onset time",
            "Description": "Time of the visual stimulus onset. T0 corresponds to when the computer was started and is"
                           "not informative in and of itself, only in relation with other events",
            "Units": "s"
        },
        "time_of_resp_vis": {
            "LongName": "Time of response to visual stimulus",
            "Description": "Time of the response to visual stimulus. time_of_resp_vis - vis_stim_time yields RT1. "
                           "Responses  were not required on every trials so many rows are empty",
            "Units": "s"
        },
        "has_response_vis": {
            "LongName": "Response to visual stimulus",
            "Description": "Whether participant provided a response to the visual stimulus in the current trial",
            "Levels": {
                "0": "No response",
                "1": "Response"
            },
        },
        "trial_response_vis": {
            "LongName": "Accuracy of the response given to visual stimuli",
            "Description": "Encoding of the accuracy of the provided response",
            "Levels": {
                "cr": "Correct rejection: did not press button when stimulus was not a target (CORRECT)",
                "hit": "Did press the button when the target was presented (CORRECT)",
                "miss": "Did not press a button when a target was presented (WRONG)",
                "fa": "false-alarm: Pressed a button when a non-target stimulus was presented (WRONG)"
            },
        },
        "aud_stim_buff": {
            "LongName": "Auditory stimulus buffer",
            "Description": "Number of the memory buffer corresponding to the auditory stimulus of the specified pitch",
            "Levels": {
                "1": "Audio buffer 1",
                "2": "Audio buffer 2"
            },
        },
        "aud_stim_time": {
            "LongName": "Time of the auditory stimulus",
            "Description": "Recorded onset time of the auditory stimulus (by PTB)",
            "Units": "s",
        },
        "aud_resp": {
            "LongName": "Auditory stimulus response",
            "Description": "Tone pitch reported by the participant",
            "Levels": {
                "1000": "Participant report that the auditory stimulus was low pitch",
                "1100": "Participant report that the auditory stimulus was high pitch"
            },
            "Units": "Hz",
        },
        "trial_accuracy_aud": {
            "LongName": "Accuracy of auditory response",
            "Description": "Encoding of auditory pitch response accuracy",
            "Levels": {
                "0": "Wrong response (respond high when low or low when high)",
                "1": "Correct response (respond high when high or low when low)",
                "NaN": "No response provided"
            }
        },
        "time_of_resp_aud": {
            "LongName": "Time of response to auditory stimulus",
            "Description": "Time of the  response to auditory stimulus. aud_stim_time - time_of_resp_aud yields RT2.",
            "Units": "s"
        },
        "trial_first_button_press": {
            "LongName": "First button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine)",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant first pressed for T1",
                "1000": "Participant first pressed T2 low pitch",
                "1100": "Participant first pressed T2 high pitch"
            }
        },
        "trial_second_button_press": {
            "LongName": "Second button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine)",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant pressed for T1 second",
                "1000": "Participant pressed T2 low pitch second",
                "1100": "Participant pressed T2 high pitch second"
            }
        },
        "fix_time": {
            "LongName": "Time of blank screen onset",
            "Description": "Time stamp at which the visual stimulus disappears (T1 offset). Each trial lasts 2 sec + "
                           "jitter. The duration of the blank screen therefore depends on T1 duration",
            "Units": "s"
        },
        "JitOnset": {
            "LongName": "Onset of ITI jitter",
            "Description": "Time at which the fixed 2s of a trial have ended and the random ITI starts",
            "Units": "s"
        },
        "trial_end": {
            "LongName": "Timestamp of trial end",
            "Description": "Time at which the current trial is over and the next one starts",
            "Units": "s"
        },
        "wrong_key": {
            "LongName": "Wrong key code",
            "Description": "Record if the participant pressed a wrong key during the experiment",
            "Units": "a.u."
        },
        "wrong_key_timestemp": {
            "LongName": "Wrong key time stamp",
            "Description": "Time stamp at which a wrong key was pressed",
            "Units": "s"
        },
        "TargetScreenOnset": {
            "LongName": "Time stamp of target screen onset",
            "Description": "Time stamp at which the target screen is presented to the participant",
            "Units": "s"
        },
        "RT_vis": {
            "LongName": "Reaction time to visual stimulus (RT1)",
            "Description": "Difference between T1 onset and response (time_of_resp_vis - vis_stim_time)",
            "Units": "s"
        },
        "RT_aud": {
            "LongName": "Reaction time to auditory stimulus (RT2)",
            "Description": "Difference between T2 onset and response (time_of_resp_aud - aud_stim_time)",
            "Units": "s"
        },
        "is_duplicated": {
            "LongName": "Is trial duplicated",
            "Description": "Identify trials that were repeated twice. In a few cases, the experiment had to be "
                           "restarted from the last block. This enables keeping only the latest data",
            "Levels": {
                "False": "This trial was not repeated",
                "True": "This trial was repeated"
            }
        },
    },
    "introspection": {
        "sub_id": {
            "LongName": "Participant ID",
            "Description": "Subject identifier",
        },
        "task": {
            "LongName": "Task",
            "Description": "Task this log file corresponds to",
            "Levels": {
                "introspection": "introspection task"
            }
        },
        "is_practice": {
            "LongName": "Is practice",
            "Description": "Task is practice or actual experiment",
            "Levels": {
                0: "Not practice",
                1: "Practice"
            }
        },
        "Block": {
            "LongName": "Block number",
            "Description": "Block number of this trial. At the beginning of each block, a new target pair is presented",
            "Units": "a.u."
        },
        "Trial": {
            "LongName": "Trial number",
            "Description": "Number of the trial within this block",
            "Units": "a.u."
        },
        "target_01": {
            "LongName": "First visual target",
            "Description": "Name of the first target stimulus",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities",
            }
        },
        "target_02": {
            "LongName": "Second visual target",
            "Description": "Name of the second target stimulus",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities"
            }
        },
        "task_relevance": {
            "LongName": "Task relevance",
            "Description": "Task relevance of the stimulus presented in this trial",
            "Levels": {
                "non-target": "Stimulus of the same category but different identity than the targets",
                "irrelevant": "Stimulus of a different category than the targets",
                "target": "Same stimulus identity as targets"
            }
        },
        "category": {
            "LongName": "Category",
            "Description": "Category of the presented stimulus",
            "Levels": {
                "face": "Face stimulus",
                "object": "Object stimulus",
                "letter": "Letter stimulus",
                "false": "False stimulus"
            }
        },
        "orientation": {
            "LongName": "Orientation",
            "Description": "Orientation of the presented stimulus",
            "Levels": {
                "center": "Center facing stimulus",
                "left": "Left (-30°) facing stimulus",
                "right": "Right (30°) facing stimulus"
            }
        },
        "duration": {
            "LongName": "Duration",
            "Description": "Duration for which the stimulus remained on the screen",
            "Levels": {
                "0.5": "Stimulus presented for 0.5 seconds",
                "1.0": "Stimulus presented for 1.0 seconds",
                "1.5": "Stimulus presented for 1.5 seconds"
            },
            "Units": "s"
        },
        "stim_jit": {
            "LongName": "Stimulus jitter",
            "Description": "Random jitter added after the current trial, to randomize the next stimulus onset time. The"
                           "jitter was generated from a truncated exponential distribution with mean of 1s",
            "Units": "s"
        },
        "SOA": {
            "LongName": "Stimulus onset asynchrony",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset or offset",
            "Levels": {
                "0.0": "Tone presented at 0s delay from event",
                "0.116": "Tone presented at 0.116s delay from event",
                "0.232": "Tone presented at 0.232s delay from event",
                "0.466": "Tone presented at 0.466s delay from event",
            },
            "Units": "s"
        },
        "onset_SOA": {
            "LongName": "Stimulus onset asynchrony from visual stimulus onset",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset. If the tone is presented "
                           "relative to the stimulus offset, this variable takes the value of column SOA + column "
                           "duration",
            "Levels": {
                "0.0": "Tone presented at 0s delay from T1 onset",
                "0.116": "Tone presented at 0.116s delay from T1 onset",
                "0.232": "Tone presented at 0.232s delay from T1 onset",
                "0.466": "Tone presented at 0.466s delay from T1 onset",
                "0.5": "Tone presented at 0s delay from 0.5 T1 offset",
                "0.616": "Tone presented at 0.116s delay from 0.5 T1 offset",
                "0.732": "Tone presented at 0.232s delay from 0.5 T1 offset",
                "0.966": "Tone presented at 0.466s delay from 0.5 T1 offset",
                "1.0": "Tone presented at 0s delay from 1.0 T1 offset",
                "1.116": "Tone presented at 0.116s delay 1.0 T1 offset",
                "1.232": "Tone presented at 0.232s delay 1.0 T1 offset",
                "1.466": "Tone presented at 0.466s delay 1.0 T1 offset",
                "1.5": "Tone presented at 0s delay from 1.5 T1 offset",
                "1.616": "Tone presented at 0.116s delay 1.5 T1 offset",
                "1.732": "Tone presented at 0.232s delay 1.5 T1 offset",
                "1.966": "Tone presented at 0.466s delay 1.5 T1 offset",
            },
            "Units": "s"
        },
        "SOA_lock": {
            "LongName": "Lock of auditory tone onset asynchrony",
            "Description": "Whether the auditory tone was presented relative to the onset or offset of T1 stimulus",
            "Levels": {
                "onset": "Tone presented relative to T1 onset",
                "offset": "Tone presented relative to T1 offset"
            }
        },
        "pitch": {
            "LongName": "Auditory stimulus (T2) pitch",
            "Description": "Pitch of the auditory stimulus",
            "Levels": {
                "1000": "Low pitch",
                "1100": "High pitch"
            },
            "Units": "Hz"
        },
        "texture": {
            "LongName": "Texture number",
            "Description": "Number of the visual stimulus texture loaded in memory by PTB",
            "Units": "a.u."
        },
        "vis_stim_time": {
            "LongName": "Visual stimulus onset time",
            "Description": "Time of the visual stimulus onset. T0 corresponds to when the computer was started and is"
                           "not informative in and of itself, only in relation with other events",
            "Units": "s"
        },
        "time_of_resp_vis": {
            "LongName": "Time of response to visual stimulus",
            "Description": "Time of the response to visual stimulus. time_of_resp_vis - vis_stim_time yields RT1. "
                           "Responses  were not required on every trials so many rows are empty",
            "Units": "s"
        },
        "has_response_vis": {
            "LongName": "Response to visual stimulus",
            "Description": "Whether participant provided a response to the visual stimulus in the current trial",
            "Levels": {
                "0": "No response",
                "1": "Response"
            },
        },
        "trial_response_vis": {
            "LongName": "Accuracy of the response given to visual stimuli",
            "Description": "Encoding of the accuracy of the provided response",
            "Levels": {
                "cr": "Correct rejection: did not press button when stimulus was not a target (CORRECT)",
                "hit": "Did press the button when the target was presented (CORRECT)",
                "miss": "Did not press a button when a target was presented (WRONG)",
                "fa": "false-alarm: Pressed a button when a non-target stimulus was presented (WRONG)"
            },
        },
        "aud_stim_buff": {
            "LongName": "Auditory stimulus buffer",
            "Description": "Number of the memory buffer corresponding to the auditory stimulus of the specified pitch",
            "Levels": {
                "1": "Audio buffer 1",
                "2": "Audio buffer 2"
            },
        },
        "aud_stim_time": {
            "LongName": "Time of the auditory stimulus",
            "Description": "Recorded onset time of the auditory stimulus (by PTB)",
            "Units": "s",
        },
        "aud_resp": {
            "LongName": "Auditory stimulus response",
            "Description": "Tone pitch reported by the participant",
            "Levels": {
                "1000": "Participant report that the auditory stimulus was low pitch",
                "1100": "Participant report that the auditory stimulus was high pitch"
            },
            "Units": "Hz",
        },
        "trial_accuracy_aud": {
            "LongName": "Accuracy of auditory response",
            "Description": "Encoding of auditory pitch response accuracy",
            "Levels": {
                "0": "Wrong response (respond high when low or low when high)",
                "1": "Correct response (respond high when high or low when low)",
                "NaN": "No response provided"
            }
        },
        "time_of_resp_aud": {
            "LongName": "Time of response to auditory stimulus",
            "Description": "Time of the  response to auditory stimulus. aud_stim_time - time_of_resp_aud yields RT2.",
            "Units": "s"
        },
        "trial_first_button_press": {
            "LongName": "First button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine)",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant first pressed for T1",
                "1000": "Participant first pressed T2 low pitch",
                "1100": "Participant first pressed T2 high pitch"
            }
        },
        "trial_second_button_press": {
            "LongName": "Second button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine)",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant pressed for T1 second",
                "1000": "Participant pressed T2 low pitch second",
                "1100": "Participant pressed T2 high pitch second"
            }
        },
        "fix_time": {
            "LongName": "Time of blank screen onset",
            "Description": "Time stamp at which the visual stimulus disappears (T1 offset). Each trial lasts 2 sec + "
                           "jitter. The duration of the blank screen therefore depends on T1 duration",
            "Units": "s"
        },
        "JitOnset": {
            "LongName": "Onset of ITI jitter",
            "Description": "Time at which the fixed 2s of a trial have ended and the random ITI starts",
            "Units": "s"
        },
        "trial_end": {
            "LongName": "Timestamp of trial end",
            "Description": "Time at which the current trial is over and the next one starts",
            "Units": "s"
        },
        "wrong_key": {
            "LongName": "Wrong key code",
            "Description": "Record if the participant pressed a wrong key during the experiment",
            "Units": "a.u."
        },
        "wrong_key_timestemp": {
            "LongName": "Wrong key time stamp",
            "Description": "Time stamp at which a wrong key was pressed",
            "Units": "s"
        },
        "TargetScreenOnset": {
            "LongName": "Time stamp of target screen onset",
            "Description": "Time stamp at which the target screen is presented to the participant",
            "Units": "s"
        },
        "iRT_vis": {
            "LongName": "Introspective decision time to visual stimulus (iRT1)",
            "Description": "Participant report of their introspective decision time, i.e. how long they think it took "
                           "them to reach a decision to press or not to press a button after T1 onset",
            "Units": "ms"
        },
        "iRT_aud": {
            "LongName": "Reaction time to visual stimulus (RT1)",
            "Description": "Participant report of their introspective decision time, i.e. how long they think it took "
                           "them to reach a decision which button to press following T2 onset",
            "Units": "ms"
        },
        "RT_vis": {
            "LongName": "Reaction time to visual stimulus (RT1)",
            "Description": "Difference between T1 onset and response (time_of_resp_vis - vis_stim_time)",
            "Units": "s"
        },
        "RT_aud": {
            "LongName": "Reaction time to auditory stimulus (RT2)",
            "Description": "Difference between T2 onset and response (time_of_resp_aud - aud_stim_time)",
            "Units": "s"
        },
        "is_duplicated": {
            "LongName": "Is trial duplicated",
            "Description": "Identify trials that were repeated twice. In a few cases, the experiment had to be "
                           "restarted from the last block. This enables keeping only the latest data",
            "Levels": {
                "False": "This trial was not repeated",
                "True": "This trial was repeated"
            }
        },
    },
    "auditory": {
        "sub_id": {
            "LongName": "Participant ID",
            "Description": "Subject identifier",
        },
        "task": {
            "LongName": "Task",
            "Description": "Task this log file corresponds to",
            "Levels": {
                "auditory": "audio only task"
            }
        },
        "is_practice": {
            "LongName": "Is practice",
            "Description": "Task is practice or actual experiment",
            "Levels": {
                0: "Not practice",
                1: "Practice"
            }
        },
        "Block": {
            "LongName": "Block number",
            "Description": "Block number of this trial. At the beginning of each block, a new target pair is presented",
            "Units": "a.u."
        },
        "Trial": {
            "LongName": "Trial number",
            "Description": "Number of the trial within this block",
            "Units": "a.u."
        },
        "target_01": {
            "LongName": "First visual target",
            "Description": "Name of the first target stimulus. Kept for format compatibility, no target were presented "
                           "in this task",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities",
            }
        },
        "target_02": {
            "LongName": "Second visual target",
            "Description": "Name of the second target stimulus. Kept for format compatibility, no target were presented "
                           "in this task",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities"
            }
        },
        "task_relevance": {
            "LongName": "Task relevance",
            "Description": "Task relevance of the stimulus presented in this trial. Kept for format compatibility, "
                           "no visual stimuli were presented in this task",
            "Levels": {
                "non-target": "Stimulus of the same category but different identity than the targets",
                "irrelevant": "Stimulus of a different category than the targets",
                "target": "Same stimulus identity as targets"
            }
        },
        "category": {
            "LongName": "Category",
            "Description": "Category of the presented stimulus. Kept for format compatibility, "
                           "no visual stimuli were presented in this task",
            "Levels": {
                "face": "Face stimulus",
                "object": "Object stimulus",
                "letter": "Letter stimulus",
                "false": "False stimulus"
            }
        },
        "orientation": {
            "LongName": "Orientation",
            "Description": "Orientation of the presented stimulus. Kept for format compatibility, "
                           "no visual stimuli were presented in this task",
            "Levels": {
                "center": "Center facing stimulus",
                "left": "Left (-30°) facing stimulus",
                "right": "Right (30°) facing stimulus"
            }
        },
        "duration": {
            "LongName": "Duration",
            "Description": "Duration for which the stimulus remained on the screen. Kept for format compatibility, "
                           "no visual stimuli were presented in this task",
            "Levels": {
                "0.5": "Stimulus presented for 0.5 seconds",
                "1.0": "Stimulus presented for 1.0 seconds",
                "1.5": "Stimulus presented for 1.5 seconds"
            },
            "Units": "s"
        },
        "stim_jit": {
            "LongName": "Stimulus jitter",
            "Description": "Random jitter added after the current trial, to randomize the next stimulus onset time. The"
                           "jitter was generated from a truncated exponential distribution with mean of 1s",
            "Units": "s"
        },
        "SOA": {
            "LongName": "Stimulus onset asynchrony",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset or offset",
            "Levels": {
                "0.0": "Tone presented at 0s delay from event",
                "0.116": "Tone presented at 0.116s delay from event",
                "0.232": "Tone presented at 0.232s delay from event",
                "0.466": "Tone presented at 0.466s delay from event",
            },
            "Units": "s"
        },
        "onset_SOA": {
            "LongName": "Stimulus onset asynchrony from visual stimulus onset",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset. If the tone is presented "
                           "relative to the stimulus offset, this variable takes the value of column SOA + column "
                           "duration",
            "Levels": {
                "0.0": "Tone presented at 0s delay from T1 onset",
                "0.116": "Tone presented at 0.116s delay from T1 onset",
                "0.232": "Tone presented at 0.232s delay from T1 onset",
                "0.466": "Tone presented at 0.466s delay from T1 onset",
                "0.5": "Tone presented at 0s delay from 0.5 T1 offset",
                "0.616": "Tone presented at 0.116s delay from 0.5 T1 offset",
                "0.732": "Tone presented at 0.232s delay from 0.5 T1 offset",
                "0.966": "Tone presented at 0.466s delay from 0.5 T1 offset",
                "1.0": "Tone presented at 0s delay from 1.0 T1 offset",
                "1.116": "Tone presented at 0.116s delay 1.0 T1 offset",
                "1.232": "Tone presented at 0.232s delay 1.0 T1 offset",
                "1.466": "Tone presented at 0.466s delay 1.0 T1 offset",
                "1.5": "Tone presented at 0s delay from 1.5 T1 offset",
                "1.616": "Tone presented at 0.116s delay 1.5 T1 offset",
                "1.732": "Tone presented at 0.232s delay 1.5 T1 offset",
                "1.966": "Tone presented at 0.466s delay 1.5 T1 offset",
            },
            "Units": "s"
        },
        "SOA_lock": {
            "LongName": "Lock of auditory tone onset asynchrony",
            "Description": "Whether the auditory tone was presented relative to the onset or offset of T1 stimulus",
            "Levels": {
                "onset": "Tone presented relative to T1 onset",
                "offset": "Tone presented relative to T1 offset"
            }
        },
        "pitch": {
            "LongName": "Auditory stimulus (T2) pitch",
            "Description": "Pitch of the auditory stimulus",
            "Levels": {
                "1000": "Low pitch",
                "1100": "High pitch"
            },
            "Units": "Hz"
        },
        "texture": {
            "LongName": "Texture number",
            "Description": "Number of the visual stimulus texture loaded in memory by PTB. Kept for format compatibility, "
                           "no visual stimuli were presented in this task",
            "Units": "a.u."
        },
        "vis_stim_time": {
            "LongName": "Visual stimulus onset time",
            "Description": "Time of the visual stimulus onset. T0 corresponds to when the computer was started and is"
                           "not informative in and of itself, only in relation with other events. Kept for format"
                           " compatibility, no visual stimuli were presented in this task",
            "Units": "s"
        },
        "time_of_resp_vis": {
            "LongName": "Time of response to visual stimulus",
            "Description": "Time of the response to visual stimulus. time_of_resp_vis - vis_stim_time yields RT1. "
                           "Responses  were not required on every trials so many rows are empty. Kept for format "
                           "compatibility, no visual stimuli were presented in this task",
            "Units": "s"
        },
        "has_response_vis": {
            "LongName": "Response to visual stimulus",
            "Description": "Whether participant provided a response to the visual stimulus in the current trial. Kept "
                           "for format compatibility, no visual stimuli were presented in this task",
            "Levels": {
                "0": "No response",
                "1": "Response"
            },
        },
        "trial_response_vis": {
            "LongName": "Accuracy of the response given to visual stimuli",
            "Description": "Encoding of the accuracy of the provided response. Kept for format compatibility, "
                           "no visual stimuli were presented in this task",
            "Levels": {
                "cr": "Correct rejection: did not press button when stimulus was not a target (CORRECT)",
                "hit": "Did press the button when the target was presented (CORRECT)",
                "miss": "Did not press a button when a target was presented (WRONG)",
                "fa": "false-alarm: Pressed a button when a non-target stimulus was presented (WRONG)"
            },
        },
        "aud_stim_buff": {
            "LongName": "Auditory stimulus buffer",
            "Description": "Number of the memory buffer corresponding to the auditory stimulus of the specified pitch",
            "Levels": {
                "1": "Audio buffer 1",
                "2": "Audio buffer 2"
            },
        },
        "aud_stim_time": {
            "LongName": "Time of the auditory stimulus",
            "Description": "Recorded onset time of the auditory stimulus (by PTB)",
            "Units": "s",
        },
        "aud_resp": {
            "LongName": "Auditory stimulus response",
            "Description": "Tone pitch reported by the participant",
            "Levels": {
                "1000": "Participant report that the auditory stimulus was low pitch",
                "1100": "Participant report that the auditory stimulus was high pitch"
            },
            "Units": "Hz",
        },
        "trial_accuracy_aud": {
            "LongName": "Accuracy of auditory response",
            "Description": "Encoding of auditory pitch response accuracy",
            "Levels": {
                "0": "Wrong response (respond high when low or low when high)",
                "1": "Correct response (respond high when high or low when low)",
                "NaN": "No response provided"
            }
        },
        "time_of_resp_aud": {
            "LongName": "Time of response to auditory stimulus",
            "Description": "Time of the  response to auditory stimulus. aud_stim_time - time_of_resp_aud yields RT2.",
            "Units": "s"
        },
        "trial_first_button_press": {
            "LongName": "First button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine)",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant first pressed for T1",
                "1000": "Participant first pressed T2 low pitch",
                "1100": "Participant first pressed T2 high pitch"
            }
        },
        "trial_second_button_press": {
            "LongName": "Second button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine)",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant pressed for T1 second",
                "1000": "Participant pressed T2 low pitch second",
                "1100": "Participant pressed T2 high pitch second"
            }
        },
        "fix_time": {
            "LongName": "Time of blank screen onset",
            "Description": "Time stamp at which the visual stimulus disappears (T1 offset). Each trial lasts 2 sec + "
                           "jitter. The duration of the blank screen therefore depends on T1 duration. Kept for format "
                           "compatibility, no visual stimuli were presented in this task",
            "Units": "s"
        },
        "JitOnset": {
            "LongName": "Onset of ITI jitter",
            "Description": "Time at which the fixed 2s of a trial have ended and the random ITI starts",
            "Units": "s"
        },
        "trial_end": {
            "LongName": "Timestamp of trial end",
            "Description": "Time at which the current trial is over and the next one starts",
            "Units": "s"
        },
        "wrong_key": {
            "LongName": "Wrong key code",
            "Description": "Record if the participant pressed a wrong key during the experiment",
            "Units": "a.u."
        },
        "wrong_key_timestemp": {
            "LongName": "Wrong key time stamp",
            "Description": "Time stamp at which a wrong key was pressed",
            "Units": "s"
        },
        "TargetScreenOnset": {
            "LongName": "Time stamp of target screen onset",
            "Description": "Time stamp at which the target screen is presented to the participant. Kept for format "
                           "compatibility, no visual stimuli were presented in this task",
            "Units": "s"
        },
        "RT_vis": {
            "LongName": "Reaction time to visual stimulus (RT1)",
            "Description": "Difference between T1 onset and response (time_of_resp_vis - vis_stim_time). Kept for "
                           "format compatibility, no visual stimuli were presented in this task",
            "Units": "s"
        },
        "RT_aud": {
            "LongName": "Reaction time to auditory stimulus (RT2)",
            "Description": "Difference between T2 onset and response (time_of_resp_aud - aud_stim_time)",
            "Units": "s"
        },
        "is_duplicated": {
            "LongName": "Is trial duplicated",
            "Description": "Identify trials that were repeated twice. In a few cases, the experiment had to be "
                           "restarted from the last block. This enables keeping only the latest data",
            "Levels": {
                "False": "This trial was not repeated",
                "True": "This trial was repeated"
            }
        },
    },
    "visual": {
        "sub_id": {
            "LongName": "Participant ID",
            "Description": "Subject identifier",
        },
        "task": {
            "LongName": "Task",
            "Description": "Task this log file corresponds to",
            "Levels": {
                "prp": "prp task"
            }
        },
        "is_practice": {
            "LongName": "Is practice",
            "Description": "Task is practice or actual experiment",
            "Levels": {
                0: "Not practice",
                1: "Practice"
            }
        },
        "Block": {
            "LongName": "Block number",
            "Description": "Block number of this trial. At the beginning of each block, a new target pair is presented",
            "Units": "a.u."
        },
        "Trial": {
            "LongName": "Trial number",
            "Description": "Number of the trial within this block",
            "Units": "a.u."
        },
        "target_01": {
            "LongName": "First visual target",
            "Description": "Name of the first target stimulus",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities",
            }
        },
        "target_02": {
            "LongName": "Second visual target",
            "Description": "Name of the second target stimulus",
            "Levels": {
                "face_01-20": "Face target identities",
                "object_01-20": "Object target identities",
                "letter_01-20": "Letter target identities",
                "false_01-20": "False/Symbol target identities"
            }
        },
        "task_relevance": {
            "LongName": "Task relevance",
            "Description": "Task relevance of the stimulus presented in this trial",
            "Levels": {
                "non-target": "Stimulus of the same category but different identity than the targets",
                "irrelevant": "Stimulus of a different category than the targets",
                "target": "Same stimulus identity as targets"
            }
        },
        "category": {
            "LongName": "Category",
            "Description": "Category of the presented stimulus",
            "Levels": {
                "face": "Face stimulus",
                "object": "Object stimulus",
                "letter": "Letter stimulus",
                "false": "False stimulus"
            }
        },
        "orientation": {
            "LongName": "Orientation",
            "Description": "Orientation of the presented stimulus",
            "Levels": {
                "center": "Center facing stimulus",
                "left": "Left (-30°) facing stimulus",
                "right": "Right (30°) facing stimulus"
            }
        },
        "duration": {
            "LongName": "Duration",
            "Description": "Duration for which the stimulus remained on the screen",
            "Levels": {
                "0.5": "Stimulus presented for 0.5 seconds",
                "1.0": "Stimulus presented for 1.0 seconds",
                "1.5": "Stimulus presented for 1.5 seconds"
            },
            "Units": "s"
        },
        "stim_jit": {
            "LongName": "Stimulus jitter",
            "Description": "Random jitter added after the current trial, to randomize the next stimulus onset time. The"
                           "jitter was generated from a truncated exponential distribution with mean of 1s",
            "Units": "s"
        },
        "SOA": {
            "LongName": "Stimulus onset asynchrony",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset or offset. Kept for "
                           "format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "0.0": "Tone presented at 0s delay from event",
                "0.116": "Tone presented at 0.116s delay from event",
                "0.232": "Tone presented at 0.232s delay from event",
                "0.466": "Tone presented at 0.466s delay from event",
            },
            "Units": "s"
        },
        "onset_SOA": {
            "LongName": "Stimulus onset asynchrony from visual stimulus onset",
            "Description": "Delay of the auditory tone relative to the visual stimulus onset. If the tone is presented "
                           "relative to the stimulus offset, this variable takes the value of column SOA + column. "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "0.0": "Tone presented at 0s delay from T1 onset",
                "0.116": "Tone presented at 0.116s delay from T1 onset",
                "0.232": "Tone presented at 0.232s delay from T1 onset",
                "0.466": "Tone presented at 0.466s delay from T1 onset",
                "0.5": "Tone presented at 0s delay from 0.5 T1 offset",
                "0.616": "Tone presented at 0.116s delay from 0.5 T1 offset",
                "0.732": "Tone presented at 0.232s delay from 0.5 T1 offset",
                "0.966": "Tone presented at 0.466s delay from 0.5 T1 offset",
                "1.0": "Tone presented at 0s delay from 1.0 T1 offset",
                "1.116": "Tone presented at 0.116s delay 1.0 T1 offset",
                "1.232": "Tone presented at 0.232s delay 1.0 T1 offset",
                "1.466": "Tone presented at 0.466s delay 1.0 T1 offset",
                "1.5": "Tone presented at 0s delay from 1.5 T1 offset",
                "1.616": "Tone presented at 0.116s delay 1.5 T1 offset",
                "1.732": "Tone presented at 0.232s delay 1.5 T1 offset",
                "1.966": "Tone presented at 0.466s delay 1.5 T1 offset",
            },
            "Units": "s"
        },
        "SOA_lock": {
            "LongName": "Lock of auditory tone onset asynchrony",
            "Description": "Whether the auditory tone was presented relative to the onset or offset of T1 stimulus "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "onset": "Tone presented relative to T1 onset",
                "offset": "Tone presented relative to T1 offset"
            }
        },
        "pitch": {
            "LongName": "Auditory stimulus (T2) pitch "
                        "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Description": "Pitch of the auditory stimulus",
            "Levels": {
                "1000": "Low pitch",
                "1100": "High pitch"
            },
            "Units": "Hz"
        },
        "texture": {
            "LongName": "Texture number",
            "Description": "Number of the visual stimulus texture loaded in memory by PTB",
            "Units": "a.u."
        },
        "vis_stim_time": {
            "LongName": "Visual stimulus onset time",
            "Description": "Time of the visual stimulus onset. T0 corresponds to when the computer was started and is"
                           "not informative in and of itself, only in relation with other events",
            "Units": "s"
        },
        "time_of_resp_vis": {
            "LongName": "Time of response to visual stimulus",
            "Description": "Time of the response to visual stimulus. time_of_resp_vis - vis_stim_time yields RT1. "
                           "Responses  were not required on every trials so many rows are empty",
            "Units": "s"
        },
        "has_response_vis": {
            "LongName": "Response to visual stimulus",
            "Description": "Whether participant provided a response to the visual stimulus in the current trial",
            "Levels": {
                "0": "No response",
                "1": "Response"
            },
        },
        "trial_response_vis": {
            "LongName": "Accuracy of the response given to visual stimuli",
            "Description": "Encoding of the accuracy of the provided response",
            "Levels": {
                "cr": "Correct rejection: did not press button when stimulus was not a target (CORRECT)",
                "hit": "Did press the button when the target was presented (CORRECT)",
                "miss": "Did not press a button when a target was presented (WRONG)",
                "fa": "false-alarm: Pressed a button when a non-target stimulus was presented (WRONG)"
            },
        },
        "aud_stim_buff": {
            "LongName": "Auditory stimulus buffer",
            "Description": "Number of the memory buffer corresponding to the auditory stimulus of the specified pitch "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "1": "Audio buffer 1",
                "2": "Audio buffer 2"
            },
        },
        "aud_stim_time": {
            "LongName": "Time of the auditory stimulus",
            "Description": "Recorded onset time of the auditory stimulus (by PTB) "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Units": "s",
        },
        "aud_resp": {
            "LongName": "Auditory stimulus response",
            "Description": "Tone pitch reported by the participant "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "1000": "Participant report that the auditory stimulus was low pitch",
                "1100": "Participant report that the auditory stimulus was high pitch"
            },
            "Units": "Hz",
        },
        "trial_accuracy_aud": {
            "LongName": "Accuracy of auditory response",
            "Description": "Encoding of auditory pitch response accuracy "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "0": "Wrong response (respond high when low or low when high)",
                "1": "Correct response (respond high when high or low when low)",
                "NaN": "No response provided"
            }
        },
        "time_of_resp_aud": {
            "LongName": "Time of response to auditory stimulus",
            "Description": "Time of the  response to auditory stimulus. aud_stim_time - time_of_resp_aud yields RT2. "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Units": "s"
        },
        "trial_first_button_press": {
            "LongName": "First button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine) "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant first pressed for T1",
                "1000": "Participant first pressed T2 low pitch",
                "1100": "Participant first pressed T2 high pitch"
            }
        },
        "trial_second_button_press": {
            "LongName": "Second button pressed in this trial",
            "Description": "Specifies the temporal order of button press. Participants were instructed to first decide"
                           "whether or not to press for the T1 stimulus and then T2. Trials where participants respond"
                           "first to T2 and then T1 have to be discarded. In trials where no T1 is required, T2 "
                           "will be the first and only response (which is fine) "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Levels": {
                "0": "No responses in this trial at all",
                "1": "Participant pressed for T1 second",
                "1000": "Participant pressed T2 low pitch second",
                "1100": "Participant pressed T2 high pitch second"
            }
        },
        "fix_time": {
            "LongName": "Time of blank screen onset",
            "Description": "Time stamp at which the visual stimulus disappears (T1 offset). Each trial lasts 2 sec + "
                           "jitter. The duration of the blank screen therefore depends on T1 duration",
            "Units": "s"
        },
        "JitOnset": {
            "LongName": "Onset of ITI jitter",
            "Description": "Time at which the fixed 2s of a trial have ended and the random ITI starts",
            "Units": "s"
        },
        "trial_end": {
            "LongName": "Timestamp of trial end",
            "Description": "Time at which the current trial is over and the next one starts",
            "Units": "s"
        },
        "wrong_key": {
            "LongName": "Wrong key code",
            "Description": "Record if the participant pressed a wrong key during the experiment",
            "Units": "a.u."
        },
        "wrong_key_timestemp": {
            "LongName": "Wrong key time stamp",
            "Description": "Time stamp at which a wrong key was pressed",
            "Units": "s"
        },
        "TargetScreenOnset": {
            "LongName": "Time stamp of target screen onset",
            "Description": "Time stamp at which the target screen is presented to the participant",
            "Units": "s"
        },
        "RT_vis": {
            "LongName": "Reaction time to visual stimulus (RT1)",
            "Description": "Difference between T1 onset and response (time_of_resp_vis - vis_stim_time)",
            "Units": "s"
        },
        "RT_aud": {
            "LongName": "Reaction time to auditory stimulus (RT2)",
            "Description": "Difference between T2 onset and response (time_of_resp_aud - aud_stim_time) "
                           "Kept for format compatibility, no auditory stimuli were presented in this task",
            "Units": "s"
        },
        "is_duplicated": {
            "LongName": "Is trial duplicated",
            "Description": "Identify trials that were repeated twice. In a few cases, the experiment had to be "
                           "restarted from the last block. This enables keeping only the latest data",
            "Levels": {
                "False": "This trial was not repeated",
                "True": "This trial was repeated"
            }
        },
    },
}