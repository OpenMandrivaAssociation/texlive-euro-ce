# revision 15878
# category Package
# catalog-ctan /fonts/euro-ce
# catalog-date 2007-07-29 11:53:03 +0200
# catalog-license other-free
# catalog-version undef
Name:		texlive-euro-ce
Version:	20070729
Release:	1
Summary:	Euro and CE sign font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/euro-ce
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro-ce.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro-ce.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
MetaFont source for the symbols in several variants, designed
to fit with Computer Modern-set text.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/euro-ce/ceit.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/cemac.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/cerm.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/cesl.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurobf.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurobfit.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurobfsl.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/euroit.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/euromac.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/euroof.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurorm.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurosl.mf
%{_texmfdistdir}/fonts/source/public/euro-ce/eurosp.mf
%{_texmfdistdir}/fonts/tfm/public/euro-ce/ceit.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/cerm.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/cesl.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurobf.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurobfit.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurobfsl.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/euroit.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/euroof.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurorm.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurosl.tfm
%{_texmfdistdir}/fonts/tfm/public/euro-ce/eurosp.tfm
%doc %{_texmfdistdir}/doc/fonts/euro-ce/euro-ce.doc
%doc %{_texmfdistdir}/doc/fonts/euro-ce/euro-ce.dvi
%doc %{_texmfdistdir}/doc/fonts/euro-ce/euro-ce.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
