def mixer(fresh_feed_co, fresh_feed_aa, oil_recycle, acid_recycle, out_stream):
    out_stream.mol_flow = fresh_feed_co.mol_flow + fresh_feed_aa.mol_flow + acid_recycle.mol_flow + oil_recycle.mol_flow