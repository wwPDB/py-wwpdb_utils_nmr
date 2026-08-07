
// Generated from /home/webmaster/py-wwpdb_utils_nmr/wwpdb/utils/tests-nmr/antlr-grammars-v4.10/OliviaPKParser.g4 by ANTLR 4.13.0

#pragma once


#include "antlr4-runtime.h"




class  OliviaPKParser : public antlr4::Parser {
public:
  enum {
    Typedef = 1, Separator = 2, Format = 3, Unformat = 4, Eof = 5, Null_string = 6, 
    Integer = 7, Float = 8, Real = 9, COMMENT = 10, SHARP_COMMENT = 11, 
    EXCLM_COMMENT = 12, Double_quote_string = 13, Single_quote_string = 14, 
    Simple_name = 15, SPACE = 16, RETURN = 17, SECTION_COMMENT = 18, LINE_COMMENT = 19, 
    Idx_tbl_2d = 20, Idx_tbl_3d = 21, Idx_tbl_4d = 22, Ass_tbl_2d = 23, 
    Ass_tbl_3d = 24, Ass_tbl_4d = 25, SPACE_TD = 26, RETURN_TD = 27, Tab = 28, 
    Comma = 29, Space = 30, SPACE_SE = 31, RETURN_SE = 32, Index = 33, X_ppm = 34, 
    Y_ppm = 35, Z_ppm = 36, A_ppm = 37, X_hz = 38, Y_hz = 39, Z_hz = 40, 
    A_hz = 41, Amplitude = 42, Volume = 43, Vol_err = 44, X_chain = 45, 
    Y_chain = 46, Z_chain = 47, A_chain = 48, X_resname = 49, Y_resname = 50, 
    Z_resname = 51, A_resname = 52, X_seqnum = 53, Y_seqnum = 54, Z_seqnum = 55, 
    A_seqnum = 56, X_assign = 57, Y_assign = 58, Z_assign = 59, A_assign = 60, 
    Eval = 61, Status = 62, User_memo = 63, Update_time = 64, SPACE_FO = 65, 
    RETURN_FO = 66, Printf_string = 67, SPACE_PF = 68, RETURN_PF = 69, Any_name = 70, 
    SPACE_CM = 71, RETURN_CM = 72
  };

  enum {
    RuleOlivia_pk = 0, RuleComment = 1, RuleIdx_peak_list_2d = 2, RuleIdx_peak_2d = 3, 
    RuleIdx_peak_list_3d = 4, RuleIdx_peak_3d = 5, RuleIdx_peak_list_4d = 6, 
    RuleIdx_peak_4d = 7, RuleAss_peak_list_2d = 8, RuleAss_peak_2d = 9, 
    RuleAss_peak_list_3d = 10, RuleAss_peak_3d = 11, RuleAss_peak_list_4d = 12, 
    RuleAss_peak_4d = 13, RuleDef_2d_axis_order_ppm = 14, RuleTp_2d_axis_order_ppm = 15, 
    RuleDef_2d_axis_order_hz = 16, RuleTp_2d_axis_order_hz = 17, RuleDef_3d_axis_order_ppm = 18, 
    RuleTp_3d_axis_order_ppm = 19, RuleDef_3d_axis_order_hz = 20, RuleTp_3d_axis_order_hz = 21, 
    RuleDef_4d_axis_order_ppm = 22, RuleTp_4d_axis_order_ppm = 23, RuleDef_4d_axis_order_hz = 24, 
    RuleTp_4d_axis_order_hz = 25, RuleString = 26, RuleInteger = 27, RuleNumber = 28, 
    RuleMemo = 29
  };

  explicit OliviaPKParser(antlr4::TokenStream *input);

  OliviaPKParser(antlr4::TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options);

  ~OliviaPKParser() override;

  std::string getGrammarFileName() const override;

  const antlr4::atn::ATN& getATN() const override;

  const std::vector<std::string>& getRuleNames() const override;

  const antlr4::dfa::Vocabulary& getVocabulary() const override;

  antlr4::atn::SerializedATNView getSerializedATN() const override;


  class Olivia_pkContext;
  class CommentContext;
  class Idx_peak_list_2dContext;
  class Idx_peak_2dContext;
  class Idx_peak_list_3dContext;
  class Idx_peak_3dContext;
  class Idx_peak_list_4dContext;
  class Idx_peak_4dContext;
  class Ass_peak_list_2dContext;
  class Ass_peak_2dContext;
  class Ass_peak_list_3dContext;
  class Ass_peak_3dContext;
  class Ass_peak_list_4dContext;
  class Ass_peak_4dContext;
  class Def_2d_axis_order_ppmContext;
  class Tp_2d_axis_order_ppmContext;
  class Def_2d_axis_order_hzContext;
  class Tp_2d_axis_order_hzContext;
  class Def_3d_axis_order_ppmContext;
  class Tp_3d_axis_order_ppmContext;
  class Def_3d_axis_order_hzContext;
  class Tp_3d_axis_order_hzContext;
  class Def_4d_axis_order_ppmContext;
  class Tp_4d_axis_order_ppmContext;
  class Def_4d_axis_order_hzContext;
  class Tp_4d_axis_order_hzContext;
  class StringContext;
  class IntegerContext;
  class NumberContext;
  class MemoContext; 

  class  Olivia_pkContext : public antlr4::ParserRuleContext {
  public:
    Olivia_pkContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> RETURN();
    antlr4::tree::TerminalNode* RETURN(size_t i);
    std::vector<CommentContext *> comment();
    CommentContext* comment(size_t i);
    std::vector<Idx_peak_list_2dContext *> idx_peak_list_2d();
    Idx_peak_list_2dContext* idx_peak_list_2d(size_t i);
    std::vector<Idx_peak_list_3dContext *> idx_peak_list_3d();
    Idx_peak_list_3dContext* idx_peak_list_3d(size_t i);
    std::vector<Idx_peak_list_4dContext *> idx_peak_list_4d();
    Idx_peak_list_4dContext* idx_peak_list_4d(size_t i);
    std::vector<Ass_peak_list_2dContext *> ass_peak_list_2d();
    Ass_peak_list_2dContext* ass_peak_list_2d(size_t i);
    std::vector<Ass_peak_list_3dContext *> ass_peak_list_3d();
    Ass_peak_list_3dContext* ass_peak_list_3d(size_t i);
    std::vector<Ass_peak_list_4dContext *> ass_peak_list_4d();
    Ass_peak_list_4dContext* ass_peak_list_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Olivia_pkContext* olivia_pk();

  class  CommentContext : public antlr4::ParserRuleContext {
  public:
    CommentContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *COMMENT();
    antlr4::tree::TerminalNode *RETURN_CM();
    antlr4::tree::TerminalNode *EOF();
    std::vector<antlr4::tree::TerminalNode *> Any_name();
    antlr4::tree::TerminalNode* Any_name(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  CommentContext* comment();

  class  Idx_peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Idx_peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Idx_tbl_2d();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol_err();
    antlr4::tree::TerminalNode *X_chain();
    antlr4::tree::TerminalNode *X_resname();
    antlr4::tree::TerminalNode *X_seqnum();
    antlr4::tree::TerminalNode *X_assign();
    antlr4::tree::TerminalNode *Y_chain();
    antlr4::tree::TerminalNode *Y_resname();
    antlr4::tree::TerminalNode *Y_seqnum();
    antlr4::tree::TerminalNode *Y_assign();
    antlr4::tree::TerminalNode *Eval();
    antlr4::tree::TerminalNode *Status();
    antlr4::tree::TerminalNode *User_memo();
    antlr4::tree::TerminalNode *Update_time();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    Def_2d_axis_order_ppmContext *def_2d_axis_order_ppm();
    Tp_2d_axis_order_ppmContext *tp_2d_axis_order_ppm();
    Def_2d_axis_order_hzContext *def_2d_axis_order_hz();
    Tp_2d_axis_order_hzContext *tp_2d_axis_order_hz();
    std::vector<Idx_peak_2dContext *> idx_peak_2d();
    Idx_peak_2dContext* idx_peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Idx_peak_list_2dContext* idx_peak_list_2d();

  class  Idx_peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Idx_peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<StringContext *> string();
    StringContext* string(size_t i);
    std::vector<IntegerContext *> integer();
    IntegerContext* integer(size_t i);
    MemoContext *memo();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Idx_peak_2dContext* idx_peak_2d();

  class  Idx_peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Idx_peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Idx_tbl_3d();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol_err();
    antlr4::tree::TerminalNode *X_chain();
    antlr4::tree::TerminalNode *X_resname();
    antlr4::tree::TerminalNode *X_seqnum();
    antlr4::tree::TerminalNode *X_assign();
    antlr4::tree::TerminalNode *Y_chain();
    antlr4::tree::TerminalNode *Y_resname();
    antlr4::tree::TerminalNode *Y_seqnum();
    antlr4::tree::TerminalNode *Y_assign();
    antlr4::tree::TerminalNode *Z_chain();
    antlr4::tree::TerminalNode *Z_resname();
    antlr4::tree::TerminalNode *Z_seqnum();
    antlr4::tree::TerminalNode *Z_assign();
    antlr4::tree::TerminalNode *Eval();
    antlr4::tree::TerminalNode *Status();
    antlr4::tree::TerminalNode *User_memo();
    antlr4::tree::TerminalNode *Update_time();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    Def_3d_axis_order_ppmContext *def_3d_axis_order_ppm();
    Tp_3d_axis_order_ppmContext *tp_3d_axis_order_ppm();
    Def_3d_axis_order_hzContext *def_3d_axis_order_hz();
    Tp_3d_axis_order_hzContext *tp_3d_axis_order_hz();
    std::vector<Idx_peak_3dContext *> idx_peak_3d();
    Idx_peak_3dContext* idx_peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Idx_peak_list_3dContext* idx_peak_list_3d();

  class  Idx_peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Idx_peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<StringContext *> string();
    StringContext* string(size_t i);
    std::vector<IntegerContext *> integer();
    IntegerContext* integer(size_t i);
    MemoContext *memo();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Idx_peak_3dContext* idx_peak_3d();

  class  Idx_peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Idx_peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Idx_tbl_4d();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol_err();
    antlr4::tree::TerminalNode *X_chain();
    antlr4::tree::TerminalNode *X_resname();
    antlr4::tree::TerminalNode *X_seqnum();
    antlr4::tree::TerminalNode *X_assign();
    antlr4::tree::TerminalNode *Y_chain();
    antlr4::tree::TerminalNode *Y_resname();
    antlr4::tree::TerminalNode *Y_seqnum();
    antlr4::tree::TerminalNode *Y_assign();
    antlr4::tree::TerminalNode *Z_chain();
    antlr4::tree::TerminalNode *Z_resname();
    antlr4::tree::TerminalNode *Z_seqnum();
    antlr4::tree::TerminalNode *Z_assign();
    antlr4::tree::TerminalNode *A_chain();
    antlr4::tree::TerminalNode *A_resname();
    antlr4::tree::TerminalNode *A_seqnum();
    antlr4::tree::TerminalNode *A_assign();
    antlr4::tree::TerminalNode *Eval();
    antlr4::tree::TerminalNode *Status();
    antlr4::tree::TerminalNode *User_memo();
    antlr4::tree::TerminalNode *Update_time();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    Def_4d_axis_order_ppmContext *def_4d_axis_order_ppm();
    Tp_4d_axis_order_ppmContext *tp_4d_axis_order_ppm();
    Def_4d_axis_order_hzContext *def_4d_axis_order_hz();
    Tp_4d_axis_order_hzContext *tp_4d_axis_order_hz();
    std::vector<Idx_peak_4dContext *> idx_peak_4d();
    Idx_peak_4dContext* idx_peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Idx_peak_list_4dContext* idx_peak_list_4d();

  class  Idx_peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Idx_peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    std::vector<StringContext *> string();
    StringContext* string(size_t i);
    std::vector<IntegerContext *> integer();
    IntegerContext* integer(size_t i);
    MemoContext *memo();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Idx_peak_4dContext* idx_peak_4d();

  class  Ass_peak_list_2dContext : public antlr4::ParserRuleContext {
  public:
    Ass_peak_list_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Ass_tbl_2d();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *X_chain();
    antlr4::tree::TerminalNode *X_resname();
    antlr4::tree::TerminalNode *X_seqnum();
    antlr4::tree::TerminalNode *X_assign();
    antlr4::tree::TerminalNode *Y_chain();
    antlr4::tree::TerminalNode *Y_resname();
    antlr4::tree::TerminalNode *Y_seqnum();
    antlr4::tree::TerminalNode *Y_assign();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol_err();
    antlr4::tree::TerminalNode *Eval();
    antlr4::tree::TerminalNode *Status();
    antlr4::tree::TerminalNode *User_memo();
    antlr4::tree::TerminalNode *Update_time();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    Def_2d_axis_order_ppmContext *def_2d_axis_order_ppm();
    Tp_2d_axis_order_ppmContext *tp_2d_axis_order_ppm();
    Def_2d_axis_order_hzContext *def_2d_axis_order_hz();
    Tp_2d_axis_order_hzContext *tp_2d_axis_order_hz();
    std::vector<Ass_peak_2dContext *> ass_peak_2d();
    Ass_peak_2dContext* ass_peak_2d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ass_peak_list_2dContext* ass_peak_list_2d();

  class  Ass_peak_2dContext : public antlr4::ParserRuleContext {
  public:
    Ass_peak_2dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<StringContext *> string();
    StringContext* string(size_t i);
    std::vector<IntegerContext *> integer();
    IntegerContext* integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    MemoContext *memo();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ass_peak_2dContext* ass_peak_2d();

  class  Ass_peak_list_3dContext : public antlr4::ParserRuleContext {
  public:
    Ass_peak_list_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Ass_tbl_3d();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *X_chain();
    antlr4::tree::TerminalNode *X_resname();
    antlr4::tree::TerminalNode *X_seqnum();
    antlr4::tree::TerminalNode *X_assign();
    antlr4::tree::TerminalNode *Y_chain();
    antlr4::tree::TerminalNode *Y_resname();
    antlr4::tree::TerminalNode *Y_seqnum();
    antlr4::tree::TerminalNode *Y_assign();
    antlr4::tree::TerminalNode *Z_chain();
    antlr4::tree::TerminalNode *Z_resname();
    antlr4::tree::TerminalNode *Z_seqnum();
    antlr4::tree::TerminalNode *Z_assign();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol_err();
    antlr4::tree::TerminalNode *Eval();
    antlr4::tree::TerminalNode *Status();
    antlr4::tree::TerminalNode *User_memo();
    antlr4::tree::TerminalNode *Update_time();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    Def_3d_axis_order_ppmContext *def_3d_axis_order_ppm();
    Tp_3d_axis_order_ppmContext *tp_3d_axis_order_ppm();
    Def_3d_axis_order_hzContext *def_3d_axis_order_hz();
    Tp_3d_axis_order_hzContext *tp_3d_axis_order_hz();
    std::vector<Ass_peak_3dContext *> ass_peak_3d();
    Ass_peak_3dContext* ass_peak_3d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ass_peak_list_3dContext* ass_peak_list_3d();

  class  Ass_peak_3dContext : public antlr4::ParserRuleContext {
  public:
    Ass_peak_3dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<StringContext *> string();
    StringContext* string(size_t i);
    std::vector<IntegerContext *> integer();
    IntegerContext* integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    MemoContext *memo();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ass_peak_3dContext* ass_peak_3d();

  class  Ass_peak_list_4dContext : public antlr4::ParserRuleContext {
  public:
    Ass_peak_list_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Typedef();
    antlr4::tree::TerminalNode *Ass_tbl_4d();
    antlr4::tree::TerminalNode *RETURN_TD();
    antlr4::tree::TerminalNode *Separator();
    antlr4::tree::TerminalNode *RETURN_SE();
    antlr4::tree::TerminalNode *Format();
    antlr4::tree::TerminalNode *X_chain();
    antlr4::tree::TerminalNode *X_resname();
    antlr4::tree::TerminalNode *X_seqnum();
    antlr4::tree::TerminalNode *X_assign();
    antlr4::tree::TerminalNode *Y_chain();
    antlr4::tree::TerminalNode *Y_resname();
    antlr4::tree::TerminalNode *Y_seqnum();
    antlr4::tree::TerminalNode *Y_assign();
    antlr4::tree::TerminalNode *Z_chain();
    antlr4::tree::TerminalNode *Z_resname();
    antlr4::tree::TerminalNode *Z_seqnum();
    antlr4::tree::TerminalNode *Z_assign();
    antlr4::tree::TerminalNode *A_chain();
    antlr4::tree::TerminalNode *A_resname();
    antlr4::tree::TerminalNode *A_seqnum();
    antlr4::tree::TerminalNode *A_assign();
    antlr4::tree::TerminalNode *Index();
    antlr4::tree::TerminalNode *Amplitude();
    antlr4::tree::TerminalNode *Volume();
    antlr4::tree::TerminalNode *Vol_err();
    antlr4::tree::TerminalNode *Eval();
    antlr4::tree::TerminalNode *Status();
    antlr4::tree::TerminalNode *User_memo();
    antlr4::tree::TerminalNode *Update_time();
    antlr4::tree::TerminalNode *RETURN_FO();
    std::vector<antlr4::tree::TerminalNode *> Printf_string();
    antlr4::tree::TerminalNode* Printf_string(size_t i);
    antlr4::tree::TerminalNode *RETURN_PF();
    antlr4::tree::TerminalNode *Unformat();
    antlr4::tree::TerminalNode *Tab();
    antlr4::tree::TerminalNode *Comma();
    antlr4::tree::TerminalNode *Space();
    Def_4d_axis_order_ppmContext *def_4d_axis_order_ppm();
    Tp_4d_axis_order_ppmContext *tp_4d_axis_order_ppm();
    Def_4d_axis_order_hzContext *def_4d_axis_order_hz();
    Tp_4d_axis_order_hzContext *tp_4d_axis_order_hz();
    std::vector<Ass_peak_4dContext *> ass_peak_4d();
    Ass_peak_4dContext* ass_peak_4d(size_t i);


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ass_peak_list_4dContext* ass_peak_list_4d();

  class  Ass_peak_4dContext : public antlr4::ParserRuleContext {
  public:
    Ass_peak_4dContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    std::vector<StringContext *> string();
    StringContext* string(size_t i);
    std::vector<IntegerContext *> integer();
    IntegerContext* integer(size_t i);
    std::vector<antlr4::tree::TerminalNode *> Integer();
    antlr4::tree::TerminalNode* Integer(size_t i);
    std::vector<NumberContext *> number();
    NumberContext* number(size_t i);
    MemoContext *memo();
    antlr4::tree::TerminalNode *RETURN();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Ass_peak_4dContext* ass_peak_4d();

  class  Def_2d_axis_order_ppmContext : public antlr4::ParserRuleContext {
  public:
    Def_2d_axis_order_ppmContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_2d_axis_order_ppmContext* def_2d_axis_order_ppm();

  class  Tp_2d_axis_order_ppmContext : public antlr4::ParserRuleContext {
  public:
    Tp_2d_axis_order_ppmContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *X_ppm();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tp_2d_axis_order_ppmContext* tp_2d_axis_order_ppm();

  class  Def_2d_axis_order_hzContext : public antlr4::ParserRuleContext {
  public:
    Def_2d_axis_order_hzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_hz();
    antlr4::tree::TerminalNode *Y_hz();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_2d_axis_order_hzContext* def_2d_axis_order_hz();

  class  Tp_2d_axis_order_hzContext : public antlr4::ParserRuleContext {
  public:
    Tp_2d_axis_order_hzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *X_hz();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tp_2d_axis_order_hzContext* tp_2d_axis_order_hz();

  class  Def_3d_axis_order_ppmContext : public antlr4::ParserRuleContext {
  public:
    Def_3d_axis_order_ppmContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Z_ppm();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_3d_axis_order_ppmContext* def_3d_axis_order_ppm();

  class  Tp_3d_axis_order_ppmContext : public antlr4::ParserRuleContext {
  public:
    Tp_3d_axis_order_ppmContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *X_ppm();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tp_3d_axis_order_ppmContext* tp_3d_axis_order_ppm();

  class  Def_3d_axis_order_hzContext : public antlr4::ParserRuleContext {
  public:
    Def_3d_axis_order_hzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *Z_hz();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_3d_axis_order_hzContext* def_3d_axis_order_hz();

  class  Tp_3d_axis_order_hzContext : public antlr4::ParserRuleContext {
  public:
    Tp_3d_axis_order_hzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Z_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *X_hz();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tp_3d_axis_order_hzContext* tp_3d_axis_order_hz();

  class  Def_4d_axis_order_ppmContext : public antlr4::ParserRuleContext {
  public:
    Def_4d_axis_order_ppmContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *A_ppm();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_4d_axis_order_ppmContext* def_4d_axis_order_ppm();

  class  Tp_4d_axis_order_ppmContext : public antlr4::ParserRuleContext {
  public:
    Tp_4d_axis_order_ppmContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *A_ppm();
    antlr4::tree::TerminalNode *Z_ppm();
    antlr4::tree::TerminalNode *Y_ppm();
    antlr4::tree::TerminalNode *X_ppm();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tp_4d_axis_order_ppmContext* tp_4d_axis_order_ppm();

  class  Def_4d_axis_order_hzContext : public antlr4::ParserRuleContext {
  public:
    Def_4d_axis_order_hzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *X_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *Z_hz();
    antlr4::tree::TerminalNode *A_hz();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Def_4d_axis_order_hzContext* def_4d_axis_order_hz();

  class  Tp_4d_axis_order_hzContext : public antlr4::ParserRuleContext {
  public:
    Tp_4d_axis_order_hzContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *A_hz();
    antlr4::tree::TerminalNode *Z_hz();
    antlr4::tree::TerminalNode *Y_hz();
    antlr4::tree::TerminalNode *X_hz();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  Tp_4d_axis_order_hzContext* tp_4d_axis_order_hz();

  class  StringContext : public antlr4::ParserRuleContext {
  public:
    StringContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Simple_name();
    antlr4::tree::TerminalNode *Null_string();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  StringContext* string();

  class  IntegerContext : public antlr4::ParserRuleContext {
  public:
    IntegerContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Null_string();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  IntegerContext* integer();

  class  NumberContext : public antlr4::ParserRuleContext {
  public:
    NumberContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Integer();
    antlr4::tree::TerminalNode *Float();
    antlr4::tree::TerminalNode *Real();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  NumberContext* number();

  class  MemoContext : public antlr4::ParserRuleContext {
  public:
    MemoContext(antlr4::ParserRuleContext *parent, size_t invokingState);
    virtual size_t getRuleIndex() const override;
    antlr4::tree::TerminalNode *Double_quote_string();
    antlr4::tree::TerminalNode *Single_quote_string();
    antlr4::tree::TerminalNode *Simple_name();


    virtual std::any accept(antlr4::tree::ParseTreeVisitor *visitor) override;
   
  };

  MemoContext* memo();


  // By default the static state used to implement the parser is lazily initialized during the first
  // call to the constructor. You can call this function if you wish to initialize the static state
  // ahead of time.
  static void initialize();

private:
};

