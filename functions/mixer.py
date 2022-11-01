def mixer(fresh_feed_co, fresh_feed_aa, oil_recycle, acid_recycle, out_stream):
    'args(fresh feed co, fresh feed aa, oil recycle, acid recycle, outflow'
    # stream(number, mass_flow, mol_flow, co_frac, aco_frac, dco_frac, aa_frac, water_frac, gum_frac)
    out_stream_molflow = fresh_feed_co.mol_flow + fresh_feed_aa.mol_flow + acid_recycle.mol_flow + oil_recycle.mol_flow
    out_stream_co_delta = fresh_feed_co.mol_flow + oil_recycle.co_molflow
    out_stream_aco_delta = oil_recycle.aco_molflow
    out_stream_dco_delta = oil_recycle.dco_molflow
    out_stream_aa_delta = acid_recycle.aa_molflow + fresh_feed_aa.mol_flow
    out_stream_water_delta = acid_recycle.water_molflow
    out_stream_gum_delta = 0

    # update(new_massflow, new_molflow, co_delta, aco_delta, dco_delta, aa_delta, water_delta, gum_delta)
    out_stream.update(new_molflow = out_stream_molflow, co_delta = out_stream_co_delta, aco_delta = out_stream_aco_delta, dco_delta = out_stream_dco_delta, aa_delta = out_stream_aa_delta, water_delta = out_stream_water_delta, gum_delta = out_stream_gum_delta)
    return None