

Ich bin eingeloggt. Hier wollen wir den Titel eingeben:
`<input class="form-control" data-val="true" data-val-length="The title must be at most 100 characters long" data-val-length-max="100" data-val-required="The chapter title is required" id="Title" maxlength="100" name="Title" placeholder="Title of chapter" type="text" value="">`

Selector: #Title

Hier müssen wir drücken um den Inhalt des Chapters als Sourcecode einzugeben:
`<button aria-label="Source code" title="Source code" type="button" tabindex="-1" class="tox-tbtn" aria-disabled="false"><span class="tox-icon tox-tbtn__icon-wrap">``<svg width="24" height="24" focusable="false"><g fill-rule="nonzero">``<path d="M9.8 15.7c.3.3.3.8 0 1-.3.4-.9.4-1.2 0l-4.4-4.1a.8.8 0 010-1.2l4.4-4.2c.3-.3.9-.3 1.2 0 .3.3.3.8 0 1.1L6 12l3.8 3.7zM14.2 15.7c-.3.3-.3.8 0 1 .4.4.9.4 1.2 0l4.4-4.1c.3-.3.3-.9 0-1.2l-4.4-4.2a.8.8 0 00-1.2 0c-.3.3-.3.8 0 1.1L18 12l-3.8 3.7z"></path>``</g></svg>``</button>`
Selector: #chapterEditor > div > div:nth-child(5) > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-toolbar-overlord > div > div:nth-child(6) > button:nth-child(1)

Dies ist danach das eingabefeld:
<div role="dialog" aria-modal="true" tabindex="-1" class="tox-dialog tox-dialog--width-lg" aria-labelledby="dialog-label_7246512575961767970510545" aria-describedby="dialog-describe_7408672485971767970510545" style="position: relative;"><div role="presentation" class="tox-dialog__header"><div class="tox-dialog__title" id="dialog-label_7246512575961767970510545">Source Code</div><button type="button" aria-label="Close" title="Close" tabindex="-1" class="tox-button tox-button--icon tox-button--naked"><div class="tox-icon"><svg width="24" height="24" focusable="false"><path d="M17.3 8.2L13.4 12l3.9 3.8a1 1 0 01-1.5 1.5L12 13.4l-3.8 3.9a1 1 0 01-1.5-1.5l3.9-3.8-3.9-3.8a1 1 0 011.5-1.5l3.8 3.9 3.8-3.9a1 1 0 011.5 1.5z" fill-rule="evenodd"></path></svg></div></button></div><div class="tox-dialog__content-js" id="dialog-describe_7408672485971767970510545"><div class="tox-dialog__body"><div class="tox-dialog__body-content"><div class="tox-form"><div class="tox-form__group tox-form__group--stretched" aria-disabled="false"><textarea type="text" tabindex="-1" data-alloy-tabstop="true" class="tox-textarea"></textarea></div></div></div></div></div><div class="tox-dialog__footer"><div role="presentation" class="tox-dialog__footer-start"></div><div role="presentation" class="tox-dialog__footer-end"><button title="Cancel" type="button" tabindex="-1" data-alloy-tabstop="true" class="tox-button tox-button--secondary">Cancel</button><button title="Save" type="button" tabindex="-1" data-alloy-tabstop="true" class="tox-button">Save</button></div></div></div>
Selector: #dialog-describe_2288816756161767970629517 > div > div > div > div > textarea

danach sichern: <button title="Save" type="button" tabindex="-1" data-alloy-tabstop="true" class="tox-button">Save</button>
Selector: #kt-body > div:nth-child(11) > div > div.tox-dialog.tox-dialog--width-lg > div.tox-dialog__footer > div.tox-dialog__footer-end > button:nth-child(2)

Hier legen wir das Datum zum veröffentlichen fest. Ich würde erstmal 10 pro Tag veröffentlichen wollen. 
<div class="input-group date form_datetime bs-datetime" id="datetimepicker">
                                <input id="sdate" type="text" size="16" class="form-control flatpickr-input active" name="ScheduledRelease" autocomplete="off">
                                <span class="input-group-btn">
                                    <button class="btn btn-primary date-reset" type="button">
                                        <i class="fa fa-times"></i>
                                    </button>
                                    <button class="btn btn-primary date-set" type="button">
                                        <i class="fa fa-calendar"></i>
                                    </button>
                                </span>
                            </div>

dann absenden:
<button class="btn btn-primary" type="submit" name="action" value="publish">Publish Chapter</button>
Selector: 
#chapterEditor > div > div.text-center.form-group > button.btn.btn-primary
/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div/div[13]/button[3]