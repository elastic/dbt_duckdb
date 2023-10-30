
with source as (

    select * from {{ source('classic_models', 'user_role') }}

),

renamed as (

    select
        id as user_role_id,
        name,
        parentroleid,
        rollupdescription,
        opportunityaccessforaccountowner,
        caseaccessforaccountowner,
        contactaccessforaccountowner,
        forecastuserid,
        mayforecastmanagershare,
        lastmodifieddate,
        lastmodifiedbyid,
        systemmodstamp,
        portalaccountid,
        portaltype,
        portalrole,
        portalaccountownerid

    from source

)

select * from renamed