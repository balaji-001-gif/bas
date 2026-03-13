import frappe

custom_Fields = {
    "DocField": [
        {
            "fieldname": "bas_autocomplete_api",
            "label": "Bas Autocomplete Api",
            "fieldtype": "Small Text",
            "insert_after": "options",
            "depends_on": "eval: doc.fieldtype =='Autocomplete'",
            "description": "Bas Autocomplete API End Point For Mobile App. This will be used to fetch the autocomplete suggestions for this field.",
        },
        {
            "fieldname": "bas_validate_field_api",
            "label": "Bas Validate Field Api",
            "fieldtype": "Small Text",
            "insert_after": "bas_autocomplete_api",
            "description": "Bas Validate Field API End Point For Mobile App. This will be used to validate the data for this field.",
        },
        {
            "fieldname": "bas_location_required",
            "label": "Bas Location Required",
            "fieldtype": "Small Text",
            "insert_after": "options",
            "description": "Bas Location Required For Mobile App. if this field is set to true, then the mobile app will ask for location permission and send the location data to the server.",
        },
        {
            "fieldname": "show_in_mobile",
            "label": "Show in Mobile",
            "fieldtype": "Check",
            "insert_after": "disabled",
        },
    ]
}