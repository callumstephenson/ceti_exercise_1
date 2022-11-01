def filter(in_stream, out_stream_gum, gum):
    'gum filter function, inputs (in_stream, gum stream, rest out)'
    # simple mass balance for gum
    gum_delta_filter = in_stream.gum_molflow

    # remaining stream
    new_molflow_filter = in_stream.mol_flow - gum_delta_filter

    # update(new_massflow, new_molflow, co_delta, aco_delta, dco_delta, aa_delta, water_delta, gum_delta)
    out_stream_gum.update(new_molflow = gum_delta_filter, gum_delta = gum_delta_filter)
    in_stream.update(new_molflow = new_molflow_filter, gum_delta = (-1 * gum_delta_filter))
    return in_stream


def column1(in_stream, out_stream_top, out_stream_bottom, aa, co, dco, aco, water):
    'args(instream, topstream, bottomstream, chemicals: aa, co, dco, aco, water'
    # separation 'efficiencies'
    test = in_stream.mol_flow
    water_delta_column1 = in_stream.water_molflow
    aa_delta_column1 = in_stream.aa_molflow
    co_delta_column1 = in_stream.co_molflow * 0.005 # <--- separation factors
    dco_delta_column1 = in_stream.dco_molflow * 0.95
    aco_delta_column1 = in_stream.aco_molflow * 0.002

    # top stream
    out_stream_top_molflow = water_delta_column1 + aa_delta_column1 + co_delta_column1 + dco_delta_column1 + aco_delta_column1
    out_stream_top.update(new_molflow = out_stream_top_molflow, co_delta = co_delta_column1, aco_delta = aco_delta_column1, dco_delta = dco_delta_column1, aa_delta = aa_delta_column1, water_delta = water_delta_column1)

    #bottom stream
    out_stream_bottom_molflow = in_stream.mol_flow - out_stream_top_molflow
    bottom_delta_co = in_stream.co_molflow * 0.995
    bottom_delta_dco = in_stream.dco_molflow * 0.05
    bottom_delta_aco = in_stream.aco_molflow * 0.998
    out_stream_bottom.update(new_molflow = out_stream_bottom_molflow, co_delta = bottom_delta_co, dco_delta = bottom_delta_dco, aco_delta = bottom_delta_aco)
    return None


def column2(in_stream, out_stream_top, out_stream_bottom, aa, water):
    'args(instream, topstream, bottomstream, chemicals:aa, water'
    # separation top
    water_delta_column2 = in_stream.water_molflow
    aa_delta_column2 = in_stream.aa_molflow
    top_molflow = water_delta_column2 + aa_delta_column2
    out_stream_top.update(new_molflow = top_molflow, aa_delta = aa_delta_column2, water_delta = water_delta_column2)

    # separation bottom
    co_delta_column2 = in_stream.co_molflow
    dco_delta_column2 = in_stream.dco_molflow
    aco_delta_column2 = in_stream.aco_molflow
    bottom_molflow = in_stream.mol_flow - top_molflow
    out_stream_bottom.update(new_molflow = bottom_molflow, co_delta = co_delta_column2, dco_delta = dco_delta_column2, aco_delta = aco_delta_column2)
    return None

def acid_separator(in_stream, recycle, purge, aa, water):
    'input args(in_stream, recycle stream, purge stream, chemicals:aa, water'
    # 99mol% AA on recycle, 8mol% AA on purge
    purge_mol_flow = (in_stream.mol_flow *(0.99 - in_stream.aa_frac)) / 0.91
    recycle_mol_flow = in_stream.mol_flow - purge_mol_flow

    # purge deltas
    purge_water_delta = 0.92 * purge.mol_flow
    purge_aa_delta = 0.08 * purge.mol_flow
    purge.update(new_molflow = purge_mol_flow, aa_delta = purge_aa_delta, water_delta = purge_water_delta)

    # recycle deltas
    recycle_water_delta = 0.01 * recycle_mol_flow
    recycle_aa_delta = 0.99 * recycle_mol_flow
    recycle.update(new_molflow = recycle_mol_flow, aa_delta = recycle_aa_delta, water_delta = recycle_water_delta)
    return None