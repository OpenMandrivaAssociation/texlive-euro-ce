Name:		texlive-euro-ce
Epoch:		1
Version:	25714
Release:	2
Summary:	Euro and CE sign font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/euro-ce
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro-ce.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/euro-ce.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Metafont source for the symbols in several variants, designed
to fit with Computer Modern-set text.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
